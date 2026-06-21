<template>
  <div class="d-flex dashboard-wrapper">
    <SidebarMedicoComp />

    <main class="content flex-grow-1 p-4">
      <header class="mb-4">
        <h3 class="fw-bold mb-1 text-dark">Minha Agenda</h3>
        <p class="text-muted">Visualize e gerencie suas consultas agendadas</p>
      </header>

      <div class="section-card p-3 mb-4 d-flex justify-content-between align-items-center">
        <button class="btn btn-link text-dark p-0" @click="mudarDia(-1)">
          <i class="bi bi-chevron-left fs-5"></i>
        </button>
        <div class="text-center">
          <h5 class="fw-bold mb-0 text-dark text-capitalize">{{ formatarDataExibicao(dataAtual) }}</h5>
          <small class="text-muted">
            {{ consultasDoDia.filter(c => c.status === 'CONFIRMADA').length }} confirmadas | 
            {{ consultasDoDia.filter(c => c.status === 'AGUARDANDO_PAGAMENTO').length }} pendentes
          </small>
        </div>
        <button class="btn btn-link text-dark p-0" @click="mudarDia(1)">
          <i class="bi bi-chevron-right fs-5"></i>
        </button>
      </div>

      <div v-if="loading" class="text-center py-5">
        <div class="spinner-border text-primary-custom" role="status"></div>
      </div>

      <div v-else-if="consultasDoDia.length === 0" class="text-center py-5 text-muted bg-white rounded-4 border shadow-sm">
        <i class="bi bi-calendar-x fs-1 d-block mb-3 text-muted"></i>
        <h5>Nenhuma consulta para este dia</h5>
      </div>

      <div v-else class="d-flex flex-column gap-3">
        
        <div 
          v-for="consulta in consultasDoDia" 
          :key="consulta.id"
          class="consult-item-expanded d-flex align-items-center justify-content-between p-4 shadow-sm bg-white"
        >
          <div class="d-flex align-items-center gap-4">
            <div class="time-container text-center">
              <span class="time-hour fw-bold d-block">{{ formatHora(consulta.horario_inicio) }}</span>
              <span class="time-minutes text-muted">{{ formatMinutos(consulta.horario_inicio) }}</span>
            </div>
            
            <div>
              <h5 class="mb-1 fw-bold text-dark">{{ consulta.paciente_nome }}</h5>
              <p class="mb-1 text-muted small">
                {{ consulta.tipo_consulta || (consulta.status === 'CONFIRMADA' ? 'Retorno' : 'Primeira consulta') }}
              </p>
              <span class="text-dark fw-medium small" v-if="consulta.valor">
                R$ {{ Number(consulta.valor).toFixed(2).replace('.', ',') }}
              </span>
            </div>
          </div>

          <div class="d-flex align-items-center gap-3">
            <span class="badge px-3 py-2 rounded-pill fw-semibold" :class="badgeClass(consulta.status)">
              {{ statusLabel(consulta.status) }}
            </span>

            <button 
              v-if="consulta.status === 'CONFIRMADA' && consulta.link_video"
              class="btn btn-primary-custom px-4 py-2 rounded-3 fw-bold shadow-sm d-flex align-items-center gap-2"
              @click="iniciar(consulta)"
            >
              <i class="bi bi-camera-video-fill"></i> Iniciar
            </button>

            <button
              v-if="['CONFIRMADA', 'AGUARDANDO_PAGAMENTO'].includes(consulta.status)"
              class="btn btn-outline-danger btn-sm px-3 py-2 rounded-3 fw-semibold"
              @click="cancelarConsulta(consulta.id)"
            >
              Cancelar
            </button>
          </div>
        </div>

      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import SidebarMedicoComp from '../../components/doctor/SidebarDoctorComp.vue';
import { consultaService } from '../../services/api.js'

const router = useRouter()
const loading = ref(true)
const consultas = ref([])
const dataAtual = ref(new Date())

// Requisição e tratamento seguro de dados da API
const carregarConsultas = async () => {
  try {
    const res = await consultaService.listar()
    if (Array.isArray(res.data)) {
      consultas.value = res.data
    } else if (res.data && Array.isArray(res.data.dados)) {
      consultas.value = res.data.dados
    } else {
      consultas.value = []
    }
  } catch (e) {
    console.error('Erro ao buscar consultas:', e)
    consultas.value = []
  }
}

// Filtra e ordena as consultas pelo dia selecionado
const consultasDoDia = computed(() => {
  const d = new Date(dataAtual.value)
  d.setHours(0, 0, 0, 0)
  
  return consultas.value.filter(c => {
    if (!c.horario_inicio) return false
    const cd = new Date(c.horario_inicio)
    cd.setHours(0, 0, 0, 0)
    return cd.getTime() === d.getTime()
  }).sort((a, b) => new Date(a.horario_inicio) - new Date(b.horario_inicio))
})

// Altera o dia na navegação (+1 dia ou -1 dia)
const mudarDia = (delta) => {
  const d = new Date(dataAtual.value)
  d.setDate(d.getDate() + delta)
  dataAtual.value = d
}

// Formatações de Exibição
const formatarDataExibicao = (d) => {
  return new Date(d).toLocaleDateString('pt-BR', { weekday: 'long', day: 'numeric', month: 'long', year: 'numeric' })
}

const formatHora = (iso) => {
  if (!iso) return '--'
  return String(new Date(iso).getHours()).padStart(2, '0')
}

const formatMinutos = (iso) => {
  if (!iso) return ':--'
  return ':' + String(new Date(iso).getMinutes()).padStart(2, '0')
}

const statusLabel = (s) => {
  const map = { 
    CONFIRMADA: 'Confirmada', 
    AGUARDANDO_PAGAMENTO: 'Aguardando Pagamento', 
    CANCELADA: 'Cancelada', 
    FINALIZADA: 'Finalizada', 
    RESERVADA: 'Reservada' 
  }
  return map[s] || s
}

const badgeClass = (s) => {
  if (s === 'CONFIRMADA') return 'bg-success-soft text-success'
  if (s === 'AGUARDANDO_PAGAMENTO') return 'bg-warning-soft text-warning'
  if (s === 'CANCELADA') return 'bg-light text-muted border'
  if (s === 'FINALIZADA') return 'bg-secondary text-white'
  return 'bg-light text-dark'
}

// Ações
const iniciar = (consulta) => {
  router.push({ name: 'sala-teleconsulta', query: { consultaId: consulta.id, link: consulta.link_video } })
}

const cancelarConsulta = async (id) => {
  if (!confirm('Confirma o cancelamento desta consulta?')) return
  loading.value = true
  try {
    await consultaService.cancelar(id)
    await carregarConsultas()
  } catch (e) {
    alert('Erro ao cancelar consulta.')
  } finally {
    loading.value = false
  }
}

onMounted(async () => {
  try {
    await carregarConsultas()
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
  --color-1: #98DEF8;
  --color-2: #0468BF;
  --color-3: #0060B4;
  --color-4: #03A1E0;
  --color-5: #DFF2F0;
}

.dashboard-wrapper {
  background-color: #f0f7f7; 
  min-height: 100vh;
  font-family: 'Inter', sans-serif;
}

.btn-primary-custom {
  background-color: #0468BF;
  border: none;
  color: white;
  transition: background 0.3s ease;
}
.btn-primary-custom:hover {
  background-color: #0060B4;
  color: white;
}

.text-primary-custom {
  color: #0468BF;
}

.section-card {
  background: white;
  border-radius: 16px;
  border: 1px solid #E2E8F0;
}

.consult-item-expanded {
  border: 1px solid #e2e8f0;
  border-radius: 16px;
  transition: border-color 0.2s ease;
}
.consult-item-expanded:hover {
  border-color: #98DEF8;
}

.time-container {
  min-width: 60px;
  border-right: 2px solid #e2e8f0;
  padding-right: 20px;
}
.time-hour {
  font-size: 1.6rem;
  color: #0468BF; 
  line-height: 1.1;
}
.time-minutes {
  font-size: 0.95rem;
  font-weight: 600;
}

.bg-success-soft {
  background-color: #e6f6f4;
}
.text-success {
  color: #2e7d32 !important;
}
.bg-warning-soft {
  background-color: #fef5ea;
}
.text-warning {
  color: #f57c00 !important;
}

.btn-link {
  text-decoration: none;
}
</style>