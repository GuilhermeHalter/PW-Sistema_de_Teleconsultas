<template>
  <div class="d-flex dashboard-wrapper">
    <SidebarMedicoComp />

    <main class="content flex-grow-1 p-4">
      <header class="d-flex justify-content-between align-items-center mb-4">
        <div>
          <h3 class="fw-bold mb-1 text-dark">Histórico de Consultas</h3>
          <p class="text-muted">Visualize todas as suas consultas realizadas e agendadas</p>
        </div>
        
        <div class="search-box position-relative">
          <i class="bi bi-search position-absolute top-50 translate-middle-y ms-3 text-muted"></i>
          <input 
            type="text" 
            class="form-control ps-5 py-2 rounded-3 border-light shadow-sm text-sm" 
            placeholder="Buscar paciente..."
            v-model="busca"
          />
        </div>
      </header>

      <div class="row g-3 mb-4">
        <div class="col-md-4">
          <div class="stat-card text-center py-4">
            <h2 class="fw-bold text-dark mb-0">{{ contadores.confirmadas }}</h2>
            <p class="text-muted small mb-0">Agendadas / Confirmadas</p>
          </div>
        </div>
        <div class="col-md-4">
          <div class="stat-card text-center py-4">
            <h2 class="fw-bold text-dark mb-0">{{ contadores.finalizadas }}</h2>
            <p class="text-muted small mb-0">Finalizadas</p>
          </div>
        </div>
        <div class="col-md-4">
          <div class="stat-card text-center py-4">
            <h2 class="fw-bold text-dark mb-0">{{ contadores.canceladas }}</h2>
            <p class="text-muted small mb-0">Canceladas</p>
          </div>
        </div>
      </div>

      <div class="nav-pills-container p-1 mb-4 rounded-3 d-flex align-items-center bg-white shadow-sm border">
        <button 
          v-for="tab in tabs" 
          :key="tab.key" 
          class="btn-tab flex-grow-1"
          :class="{ active: filtroAtivo === tab.key }"
          @click="filtroAtivo = tab.key"
        >
          {{ tab.label }} ({{ tab.count }})
        </button>
      </div>

      <div v-if="loading" class="text-center py-5">
        <div class="spinner-border text-primary-custom" role="status"></div>
      </div>

      <div v-else-if="consultasFiltradas.length === 0" class="text-center py-5 text-muted bg-white rounded-4 border shadow-sm">
        <i class="bi bi-inbox fs-1 d-block mb-2 text-muted"></i>
        Nenhuma consulta encontrada
      </div>

      <div v-else class="d-flex flex-column gap-3">
        <div 
          v-for="consulta in consultasFiltradas" 
          :key="consulta.id"
          class="history-card p-4 bg-white rounded-4 border shadow-sm d-flex justify-content-between align-items-start"
        >
          <div class="d-flex gap-3">
            <div 
              class="initials-circle fw-bold"
              :class="consulta.status === 'FINALIZADA' ? 'bg-cyan-soft text-cyan-deep' : 'bg-blue-soft text-blue-deep'"
            >
              {{ getInitials(consulta.paciente_nome) }}
            </div>
            
            <div>
              <h5 class="fw-bold text-dark mb-1">{{ consulta.paciente_nome }}</h5>
              <p class="text-muted small mb-2">
                {{ consulta.tipo_consulta || (consulta.status === 'CONFIRMADA' ? 'Retorno' : 'Primeira consulta') }}
              </p>
              
              <div class="d-flex align-items-center gap-3 text-muted small mb-3">
                <span v-if="consulta.horario_inicio">
                  <i class="bi bi-calendar3 me-1"></i> {{ formatData(consulta.horario_inicio) }}
                </span>
                <span v-if="consulta.horario_inicio">
                  <i class="bi bi-clock me-1"></i> {{ formatHora(consulta.horario_inicio) }}
                </span>
                <span class="text-dark fw-medium" v-if="consulta.valor">
                  R$ {{ Number(consulta.valor).toFixed(2).replace('.', ',') }}
                </span>
              </div>

              <div class="d-flex gap-2">
                <button 
                  v-if="consulta.status === 'CONFIRMADA' && consulta.link_video"
                  class="btn btn-primary-custom btn-sm px-3 py-1.5 rounded-3 fw-semibold d-inline-flex align-items-center gap-1"
                  @click="iniciar(consulta)"
                >
                  <i class="bi bi-camera-video-fill"></i> Iniciar Teleconsulta
                </button>
                
                <button 
                  v-if="['CONFIRMADA', 'AGUARDANDO_PAGAMENTO'].includes(consulta.status)"
                  class="btn btn-outline-danger btn-sm px-3 py-1.5 rounded-3 fw-semibold"
                  @click="cancelarConsulta(consulta.id)"
                >
                  <i class="bi bi-x-circle me-1"></i> Cancelar
                </button>

                <button class="btn btn-outline-secondary-custom btn-sm px-3 py-1.5 rounded-3 fw-semibold">
                  <i class="bi bi-person me-1"></i> Ver Paciente
                </button>
              </div>
            </div>
          </div>
          
          <span class="badge px-3 py-2 rounded-pill fw-semibold" :class="badgeClass(consulta.status)">
            {{ statusLabel(consulta.status) }}
          </span>
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
const busca = ref('')
const filtroAtivo = ref('TODAS')

// Carregamento inicial com tratamento de Array seguro
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
    console.error('Erro ao buscar histórico de consultas:', e)
    consultas.value = []
  } finally {
    loading.value = false
  }
}

// Contadores para os Cards superiores baseados no Status real
const contadores = computed(() => ({
  confirmadas: consultas.value.filter(c => c.status === 'CONFIRMADA').length,
  finalizadas: consultas.value.filter(c => c.status === 'FINALIZADA').length,
  canceladas: consultas.value.filter(c => c.status === 'CANCELADA').length,
}))

// Configuração reativa das Abas mantendo os contadores dinâmicos
const tabs = computed(() => [
  { key: 'TODAS', label: 'Todas', count: consultas.value.length },
  { key: 'CONFIRMADA', label: 'Agendadas', count: contadores.value.confirmadas },
  { key: 'FINALIZADA', label: 'Finalizadas', count: contadores.value.finalizadas },
  { key: 'CANCELADA', label: 'Canceladas', count: contadores.value.canceladas },
])

// Filtro cruzado inteligente (Por Aba + Campo de Busca por nome)
const consultasFiltradas = computed(() => {
  let lista = filtroAtivo.value === 'TODAS' ? consultas.value : consultas.value.filter(c => c.status === filtroAtivo.value)
  if (busca.value) {
    lista = lista.filter(c => c.paciente_nome?.toLowerCase().includes(busca.value.toLowerCase()))
  }
  return lista
})

// Gerador automático de iniciais (ex: "Maria Silva" -> "MS")
const getInitials = (nome) => {
  if (!nome) return '?'
  return nome.split(' ').filter(n => n.length > 0).slice(0, 2).map(n => n[0]).join('').toUpperCase()
}

// Helpers de formatação e internacionalização de datas e horas
const formatData = (iso) => {
  if (!iso) return '-'
  return new Date(iso).toLocaleDateString('pt-BR', { day: '2-digit', month: 'short', year: 'numeric' })
}

const formatHora = (iso) => {
  if (!iso) return '-'
  const d = new Date(iso)
  return `${String(d.getHours()).padStart(2, '0')}:${String(d.getMinutes()).padStart(2, '0')}`
}

const statusLabel = (s) => {
  const map = { 
    CONFIRMADA: 'Confirmada', 
    AGUARDANDO_PAGAMENTO: 'Aguard. Pagamento', 
    CANCELADA: 'Cancelada', 
    FINALIZADA: 'Finalizada', 
    RESERVADA: 'Reservada' 
  }
  return map[s] || s
}

const badgeClass = (s) => {
  if (s === 'CONFIRMADA') return 'bg-primary-custom'
  if (s === 'AGUARDANDO_PAGAMENTO') return 'bg-warning-soft text-warning'
  if (s === 'FINALIZADA') return 'bg-success-soft text-success'
  if (s === 'CANCELADA') return 'bg-light text-muted border'
  return 'bg-light text-dark'
}

// Ações conectadas ao router e chamadas de API
const iniciar = (consulta) => {
  router.push({ name: 'sala-teleconsulta', query: { consultaId: consulta.id, link: consulta.link_video } })
}

const cancelarConsulta = async (id) => {
  if (!confirm('Confirmar cancelamento desta consulta?')) return
  loading.value = true
  try {
    await consultaService.cancelar(id)
    await carregarConsultas()
  } catch (e) {
    alert('Erro ao cancelar consulta. Tente novamente.')
    loading.value = false
  }
}

onMounted(carregarConsultas)
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

.search-box input {
  width: 240px;
  border: 1px solid #e2e8f0;
  font-size: 0.9rem;
}
.search-box input:focus {
  border-color: #0468BF;
  box-shadow: none;
}

.stat-card {
  background: white;
  border-radius: 16px;
  border: 1px solid #e2e8f0;
}
.stat-card h2 {
  font-size: 2.2rem;
}

.nav-pills-container {
  border-color: #e2e8f0 !important;
}
.btn-tab {
  background: transparent;
  border: none;
  padding: 10px 20px;
  font-weight: 500;
  font-size: 0.9rem;
  color: #475569;
  border-radius: 8px;
  transition: all 0.2s ease;
}
.btn-tab.active {
  background-color: #eef7ff;
  color: #0468BF;
  font-weight: 600;
}
.btn-tab:hover:not(.active) {
  background-color: #f8fafc;
  color: #111827;
}

.history-card {
  border: 1px solid #e2e8f0 !important;
  transition: border-color 0.2s;
}
.history-card:hover {
  border-color: #98DEF8 !important;
}

.btn-outline-secondary-custom {
  border: 1px solid #cbd5e1;
  background-color: #ffffff;
  color: #334155;
  font-size: 0.85rem;
  transition: all 0.2s;
}
.btn-outline-secondary-custom:hover {
  background-color: #f8fafc;
  border-color: #98DEF8;
  color: #0468BF;
}

/* Estilos de Botão do Código 2 acoplados harmonicamente */
.btn-primary-custom {
  background-color: #0468BF;
  border: none;
  color: white;
  transition: background 0.2s;
}
.btn-primary-custom:hover {
  background-color: #0060B4;
}

.initials-circle {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.95rem;
}
.bg-blue-soft { background-color: #eef7ff; }
.text-blue-deep { color: #0468BF; }
.bg-cyan-soft { background-color: #DFF2F0; }
.text-cyan-deep { color: #0060B4; }

.bg-primary-custom {
  background-color: #0468BF !important;
  color: white;
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
</style>