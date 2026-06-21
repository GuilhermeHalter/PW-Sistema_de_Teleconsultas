<template>
  <div class="d-flex dashboard-wrapper">
    <component :is="sidebarComponent" />

    <main class="content flex-grow-1 p-4">
      <header class="mb-4 d-flex justify-content-between align-items-center">
        <div>
          <h3 class="fw-bold mb-1 text-dark">Sala de Teleconsulta</h3>
          <p class="text-muted mb-0">
            <span v-if="ismedico">Consulta com {{ consulta?.paciente_nome }}</span>
            <span v-else>Consulta com {{ consulta?.medico_nome }}</span>
          </p>
        </div>
        <div class="d-flex align-items-center gap-2">
          <span v-if="linkConsulta" class="badge bg-success-light text-success fw-semibold px-3 py-2 rounded-pill">
            <i class="bi bi-circle-fill me-1 blink" style="font-size:0.5rem;vertical-align:middle"></i>Ao Vivo
          </span>
          <button class="btn btn-outline-danger btn-sm rounded-3 fw-semibold px-3" @click="encerrar">
            <i class="bi bi-telephone-x me-1"></i>Encerrar
          </button>
        </div>
      </header>

      <div v-if="loading" class="text-center py-5">
        <div class="spinner-border text-primary" role="status"></div>
        <p class="text-muted mt-2">Carregando sala...</p>
      </div>

      <div v-else-if="!linkConsulta" class="section-card p-5 text-center">
        <i class="bi bi-camera-video-off fs-1 text-muted d-block mb-3"></i>
        <h5 class="text-muted">Sala indisponível</h5>
        <p class="text-muted small">O link da consulta não está disponível. Verifique se o pagamento foi confirmado.</p>
        <button class="btn btn-primary-custom mt-3 px-4 rounded-3" @click="voltar">
          <i class="bi bi-arrow-left me-1"></i>Voltar
        </button>
      </div>

      <div v-else class="row g-4">
        <div class="col-lg-9">
          <div class="section-card overflow-hidden">
            <iframe
              :src="jitsiUrl"
              allow="camera; microphone; fullscreen; display-capture; autoplay"
              style="width:100%;height:600px;border:none;"
            ></iframe>
          </div>
        </div>

        <div class="col-lg-3">
          <div class="section-card p-4 h-100 d-flex flex-column">
            <h6 class="fw-bold mb-3 text-dark"><i class="bi bi-info-circle me-2 text-azure"></i>Detalhes</h6>

            <div v-if="consulta" class="d-flex flex-column gap-2 flex-grow-1">
              <div class="detail-item">
                <small class="text-muted d-block">Médico</small>
                <span class="fw-semibold small text-dark">{{ consulta.medico_nome }}</span>
              </div>
              <div class="detail-item">
                <small class="text-muted d-block">Paciente</small>
                <span class="fw-semibold small text-dark">{{ consulta.paciente_nome }}</span>
              </div>
              <div class="detail-item">
                <small class="text-muted d-block">Data</small>
                <span class="fw-semibold small text-dark">{{ formatDataHora(consulta.horario_inicio) }}</span>
              </div>
              <div class="detail-item">
                <small class="text-muted d-block">Código</small>
                <span class="fw-bold text-azure font-monospace small">{{ consulta.codigo_acesso || '—' }}</span>
              </div>
              <div class="detail-item">
                <small class="text-muted d-block">Status</small>
                <span class="badge bg-success-light text-success">Confirmada</span>
              </div>
              <div class="detail-item">
                <small class="text-muted d-block">Plataforma</small>
                <span class="badge bg-jitsi text-white small">
                  <i class="bi bi-camera-video-fill me-1"></i>Jitsi Meet
                </span>
              </div>
            </div>

            <hr class="my-3" />
            <button class="btn btn-outline-secondary-custom btn-sm rounded-3 py-2 mb-2" @click="copiarLink">
              <i class="bi bi-link-45deg me-1"></i>Copiar Link
            </button>
            <div v-if="linkCopiado" class="text-center text-success small mb-2">
              <i class="bi bi-check-circle me-1"></i>Copiado!
            </div>

            <div v-if="ismedico" class="mt-2">
              <button class="btn btn-warning btn-sm rounded-3 w-100 fw-semibold" @click="finalizarConsulta">
                <i class="bi bi-check-circle me-1"></i>Finalizar Consulta
              </button>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import SidebarPatientComp from '../../components/patient/SidebarPatientComp.vue'
import SidebarDoctorComp from '../../components/doctor/SidebarDoctorComp.vue'
import { consultaService } from '../../services/api.js'

const route = useRoute()
const router = useRouter()

const loading = ref(true)
const consulta = ref(null)
const linkConsulta = ref('')
const linkCopiado = ref(false)

const consultaId = route.query.consultaId
const linkParam = route.query.link

const role = localStorage.getItem('user_role')
const ismedico = role === 'MEDICO'
const sidebarComponent = ismedico ? SidebarDoctorComp : SidebarPatientComp

// Lógica de URL adaptada para travar privilégios do paciente
const jitsiUrl = computed(() => {
  if (!linkConsulta.value) return ''
  const roomName = linkConsulta.value.split('/').pop()
  
  // Configurações base aplicadas para ambos (médico e paciente)
  let url = `https://meet.jit.si/${roomName}#config.prejoinPageEnabled=false`
  
  if (!ismedico) {
    // 1. Remove os privilégios de moderador do paciente
    url += '&config.roles.moderator=false'
    url += '&config.remoteVideoMenu.disableKick=true' 
    url += '&config.disableRemoteMute=true'
    

    
    // 3. Remove o botão "Convidar pessoas" e compartilhamento de links da barra de ferramentas do Jitsi
    // Aqui nós redefinimos os botões visíveis para o paciente, tirando o 'invite' e 'info'
    url += '&config.toolbarButtons=["camera","microphone","closedcaptions","desktop","fullscreen","factions","hangup","profile","chat","raisehand","videoquality","filmstrip","tileview","shortcuts","help","mute-everyone"]'
    
    // 4. Garante que as travas de segurança de convites ocultem o link dentro da chamada
    url += '&config.hideConferenceSubject=true'
    url += '&config.hideConferenceTimer=false'
  }
  
  return url
})

const formatDataHora = (iso) => {
  if (!iso) return '—'
  return new Date(iso).toLocaleString('pt-BR', { day: '2-digit', month: 'short', year: 'numeric', hour: '2-digit', minute: '2-digit' })
}

const copiarLink = async () => {
  try {
    await navigator.clipboard.writeText(linkConsulta.value)
    linkCopiado.value = true
    setTimeout(() => { linkCopiado.value = false }, 2000)
  } catch {}
}

const finalizarConsulta = async () => {
  if (!confirm('Finalizar a consulta?')) return
  try {
    if (consultaId) await consultaService.finalizar(consultaId)
  } catch (e) { console.error(e) }
  voltar()
}

const encerrar = async () => {
  if (!confirm('Confirma o encerramento da consulta?')) return
  try {
    if (consultaId && ismedico) await consultaService.finalizar(consultaId)
  } catch {}
  voltar()
}

const voltar = () => {
  if (ismedico) router.push({ name: 'dashboard-medico' })
  else router.push({ name: 'historico-consultas' })
}

onMounted(async () => {
  if (linkParam) linkConsulta.value = linkParam
  if (consultaId) {
    try {
      const res = await consultaService.buscarPorId(consultaId)
      consulta.value = res.data
      if (res.data.link_video) linkConsulta.value = res.data.link_video
    } catch (e) { console.error(e) }
  }
  loading.value = false
})
</script>

<style scoped>
@import url("https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css");
.dashboard-wrapper { background-color: #f0f7f7; min-height: 100vh; }
.section-card { background: white; border-radius: 20px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); }
.detail-item { padding: 8px 0; border-bottom: 1px solid #f1f5f9; }
.detail-item:last-child { border-bottom: none; }
.btn-primary-custom { background-color: #0468BF; border: none; color: white; }
.btn-outline-secondary-custom { border: 1px solid #cbd5e1; background: white; color: #475569; }
.btn-outline-secondary-custom:hover { border-color: #98DEF8; color: #0468BF; }
.text-azure { color: #03A1E0; }
.bg-success-light { background-color: #dcfce7; }
.text-success { color: #16a34a !important; }
.bg-jitsi { background-color: #2196F3; }
@keyframes blink { 0%, 100% { opacity: 1; } 50% { opacity: 0.2; } }
.blink { animation: blink 1.5s infinite; }
</style>