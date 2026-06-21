<template>
  <div class="d-flex dashboard-wrapper">
    <SidebarMedicoComp />

    <main class="content flex-grow-1 p-4">
      <header class="d-flex justify-content-between align-items-center mb-4">
        <div>
          <h3 class="fw-bold mb-1 text-dark">Olá, {{ medicoNome }}!</h3>
          <p class="text-muted">Bem-vindo ao seu painel de teleconsultas</p>
        </div>
      </header>

      <div class="row g-3 mb-5">
        <div class="col-md-3">
          <div class="stat-card blue-theme d-flex align-items-center gap-3">
            <div class="icon-box"><i class="bi bi-calendar-check"></i></div>
            <div>
              <h4 class="mb-0 fw-bold">{{ consultasHoje.length }}</h4>
              <p class="mb-0 text-muted small">Consultas Hoje</p>
            </div>
          </div>
        </div>
        <div class="col-md-3">
          <div class="stat-card cyan-theme d-flex align-items-center gap-3">
            <div class="icon-box"><i class="bi bi-people"></i></div>
            <div>
              <h4 class="mb-0 fw-bold">{{ totalConsultas }}</h4>
              <p class="mb-0 text-muted small">Total de Consultas</p>
            </div>
          </div>
        </div>
        <div class="col-md-3">
          <div class="stat-card default-theme d-flex align-items-center gap-3">
            <div class="icon-box"><i class="bi bi-calendar-event"></i></div>
            <div>
              <h4 class="mb-0 fw-bold">{{ consultasConfirmadas }}</h4>
              <p class="mb-0 text-muted small">Confirmadas</p>
            </div>
          </div>
        </div>
        <div class="col-md-3">
          <div class="stat-card default-theme d-flex align-items-center gap-3">
            <div class="icon-box"><i class="bi bi-hourglass-split"></i></div>
            <div>
              <h4 class="mb-0 fw-bold">{{ consultasPendentes }}</h4>
              <p class="mb-0 text-muted small">Aguardando Pagamento</p>
            </div>
          </div>
        </div>
      </div>

      <div v-if="loading" class="text-center py-5">
        <div class="spinner-border text-primary" role="status"></div>
        <p class="text-muted mt-2">Carregando consultas...</p>
      </div>

      <div v-else class="row g-4">
        <div class="col-lg-8">
          <div class="section-card p-4 h-100">
            <div class="d-flex justify-content-between align-items-center mb-4">
              <h5 class="fw-bold mb-0">Consultas de Hoje</h5>
              <router-link to="/minha-agenda" class="text-decoration-none small text-secondary-custom">Ver agenda <i class="bi bi-chevron-right"></i></router-link>
            </div>

            <div v-if="consultasHoje.length === 0" class="text-center py-4 text-muted">
              <i class="bi bi-calendar-x fs-2 d-block mb-2"></i>
              Nenhuma consulta para hoje
            </div>

            <div v-else class="consult-list d-flex flex-column gap-3">
              <div
                v-for="consulta in consultasHoje"
                :key="consulta.id"
                class="consult-item d-flex align-items-center justify-content-between p-3"
              >
                <div class="d-flex align-items-center gap-3">
                  <div class="initials-circle bg-blue-soft text-blue-deep">
                    {{ formatHorario(consulta.horario_inicio) }}
                  </div>
                  <div>
                    <h6 class="mb-0 fw-bold">{{ consulta.paciente_nome }}</h6>
                    <small :class="statusClass(consulta.status)" class="fw-semibold small">
                      <i :class="statusIcon(consulta.status)"></i> {{ statusLabel(consulta.status) }}
                    </small>
                  </div>
                </div>
                <button
                  v-if="consulta.status === 'CONFIRMADA' && consulta.link_video"
                  class="btn btn-outline-primary-custom btn-sm px-3 fw-bold"
                  @click="iniciarConsulta(consulta)"
                >
                  <i class="bi bi-camera-video-fill me-1"></i> Iniciar
                </button>
                <button v-else class="btn btn-outline-secondary btn-sm px-3 fw-bold" disabled>
                  <i class="bi bi-camera-video-off-fill me-1"></i> Pendente
                </button>
              </div>
            </div>
          </div>
        </div>

        <div class="col-lg-4">
          <div class="section-card p-4 h-100">
            <div class="d-flex justify-content-between align-items-center mb-4">
              <h5 class="fw-bold mb-0"><i class="bi bi-clock-history me-2 text-azure"></i>Próximas</h5>
              <span class="badge rounded-pill bg-blue-deep">{{ proximasConsultas.length }}</span>
            </div>

            <div v-if="proximasConsultas.length === 0" class="text-center py-4 text-muted small">
              Sem consultas futuras agendadas
            </div>

            <div v-else class="notification-list d-flex flex-column gap-3">
              <div
                v-for="consulta in proximasConsultas"
                :key="consulta.id"
                class="notification-item p-3"
                :class="{ 'active-notify': consulta.status === 'CONFIRMADA' }"
              >
                <p class="mb-1 small fw-medium">{{ consulta.paciente_nome }}</p>
                <small class="text-muted">{{ formatDataHora(consulta.horario_inicio) }}</small>
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import SidebarMedicoComp from '../../components/doctor/SidebarDoctorComp.vue'
import { consultaService, medicoService } from '../../services/api.js'

const router = useRouter()
const loading = ref(true)
const consultas = ref([])
const medicoNome = ref('Médico')

const hoje = new Date()
hoje.setHours(0, 0, 0, 0)

const consultasHoje = computed(() =>
  consultas.value.filter(c => {
    if (!c.horario_inicio) return false
    const d = new Date(c.horario_inicio)
    d.setHours(0, 0, 0, 0)
    return d.getTime() === hoje.getTime()
  })
)

const proximasConsultas = computed(() =>
  consultas.value.filter(c => {
    if (!c.horario_inicio) return false
    const d = new Date(c.horario_inicio)
    d.setHours(0, 0, 0, 0)
    return d.getTime() > hoje.getTime() && ['CONFIRMADA', 'AGUARDANDO_PAGAMENTO'].includes(c.status)
  }).slice(0, 5)
)

const totalConsultas = computed(() => consultas.value.length)
const consultasConfirmadas = computed(() => consultas.value.filter(c => c.status === 'CONFIRMADA').length)
const consultasPendentes = computed(() => consultas.value.filter(c => c.status === 'AGUARDANDO_PAGAMENTO').length)

const formatHorario = (iso) => {
  if (!iso) return '--:--'
  const d = new Date(iso)
  return `${String(d.getHours()).padStart(2,'0')}:${String(d.getMinutes()).padStart(2,'0')}`
}

const formatDataHora = (iso) => {
  if (!iso) return '-'
  const d = new Date(iso)
  return d.toLocaleString('pt-BR', { day: '2-digit', month: 'short', hour: '2-digit', minute: '2-digit' })
}

const statusLabel = (s) => {
  const map = { CONFIRMADA: 'Confirmada', AGUARDANDO_PAGAMENTO: 'Aguardando Pagamento', CANCELADA: 'Cancelada', FINALIZADA: 'Finalizada', RESERVADA: 'Reservada' }
  return map[s] || s
}

const statusClass = (s) => {
  if (s === 'CONFIRMADA') return 'text-success-custom'
  if (s === 'AGUARDANDO_PAGAMENTO') return 'text-warning-custom'
  return 'text-muted'
}

const statusIcon = (s) => {
  if (s === 'CONFIRMADA') return 'bi bi-check-circle-fill me-1'
  if (s === 'AGUARDANDO_PAGAMENTO') return 'bi bi-exclamation-circle-fill me-1'
  return 'bi bi-circle me-1'
}

const iniciarConsulta = (consulta) => {
  router.push({ name: 'sala-teleconsulta', query: { consultaId: consulta.id, link: consulta.link_video } })
}

onMounted(async () => {
  try {
    const [meRes, consultasRes] = await Promise.all([
      medicoService.getMe(),
      consultaService.listar()
    ])
    medicoNome.value = `Dr(a). ${meRes.data.nomeCompleto.split(' ')[0]}`
    consultas.value = consultasRes.data
  } catch (e) {
    console.error(e)
  } finally {
    loading.value = false
  }
})
</script>

<style scoped>
@import url("https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css");

:root {
  --color-1: #98DEF8; --color-2: #0468BF; --color-3: #0060B4; --color-4: #03A1E0; --color-5: #DFF2F0;
}

.dashboard-wrapper { background-color: #f0f7f7; min-height: 100vh; font-family: 'Inter', sans-serif; }

.btn-primary-custom { background-color: #0468BF; border: none; color: white; transition: background 0.3s ease; }
.btn-primary-custom:hover { background-color: #0060B4; color: white; }

.btn-outline-primary-custom { border: 1px solid #0468BF; color: #0468BF; background: transparent; }
.btn-outline-primary-custom:hover { background: #0468BF; color: white; }

.stat-card { padding: 20px; border-radius: 16px; border: 1px solid #E2E8F0; background: white; transition: transform 0.2s; }
.stat-card:hover { transform: translateY(-3px); }
.stat-card.blue-theme { background-color: #eef7ff; border-color: #98DEF8; }
.stat-card.cyan-theme { background-color: #DFF2F0; border-color: #b8e2de; }
.stat-card .icon-box { width: 48px; height: 48px; background: #03A1E0; color: white; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 1.4rem; }
.stat-card.blue-theme .icon-box { background-color: #0468BF; }

.section-card { background: white; border-radius: 16px; border: 1px solid #E2E8F0; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); }

.consult-item { border: 1px solid #f1f5f9; background-color: #ffffff; border-radius: 12px; transition: all 0.2s; }
.consult-item:hover { border-color: #98DEF8; background-color: #fcfdfe; }

.initials-circle { width: 54px; height: 54px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 0.9rem; }
.bg-blue-soft { background-color: #eef7ff; } .text-blue-deep { color: #0468BF; }
.bg-cyan-soft { background-color: #DFF2F0; } .text-cyan-deep { color: #0060B4; }

.notification-item { background-color: #f8fafc; border-radius: 10px; border-left: 4px solid transparent; }
.active-notify { border-left-color: #03A1E0; background-color: #f0f9ff; }

.bg-blue-deep { background-color: #0468BF; } .text-secondary-custom { color: #03A1E0; font-weight: 600; }
.text-success-custom { color: #0468BF; } .text-warning-custom { color: #f57c00; }
.text-azure { color: #03A1E0; }
</style>
