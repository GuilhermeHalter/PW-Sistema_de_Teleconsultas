<template>
  <div class="dashboard-wrapper d-flex">
    <SidebarPatientComp />

    <main class="content flex-grow-1 p-4">
      <header class="mb-4">
        <h3 class="fw-bold text-dark mb-1">Histórico de Consultas</h3>
        <p class="text-muted">Visualize todas as suas consultas passadas e futuras</p>
      </header>

      <div class="tabs-container mb-4">
        <button 
          v-for="tab in tabs" 
          :key="tab.key"
          :class="['tab-item', activeTab === tab.key ? 'active' : '']"
          @click="activeTab = tab.key"
        >
          {{ tab.label }} ({{ tab.count }})
        </button>
      </div>

      <div v-if="loading" class="text-center py-5">
        <div class="spinner-border text-primary" role="status"></div>
        <p class="text-muted mt-2">Carregando consultas...</p>
      </div>

      <div v-else-if="consultasFiltradas.length === 0" class="text-center py-5 text-muted">
        <i class="bi bi-inbox fs-1 d-block mb-2"></i>
        Nenhuma consulta encontrada nesta categoria.
      </div>

      <div v-else class="consult-list d-flex flex-column gap-4">
        <div 
          v-for="consulta in consultasFiltradas" 
          :key="consulta.id"
          class="consult-card p-4"
          :class="{ 'card-cancelled': consulta.status === 'CANCELADA' }"
        >
          <div class="d-flex justify-content-between align-items-start">
            <div class="d-flex gap-4">
              <div class="avatar-circle">
                {{ getInitials(consulta.medico_nome) }}
              </div>

              <div class="info">
                <h5 class="fw-bold text-dark mb-1">{{ consulta.medico_nome }}</h5>
                <p class="specialty-text mb-2 small">
                  {{ consulta.medico_especialidade || 'Teleconsulta' }}
                </p>

                <div class="details d-flex align-items-center gap-3 mb-3">
                  <span v-if="consulta.horario_inicio" class="d-flex align-items-center gap-1">
                    <i class="bi bi-calendar3"></i> {{ formatData(consulta.horario_inicio) }}
                  </span>
                  <span v-if="consulta.horario_inicio" class="d-flex align-items-center gap-1">
                    <i class="bi bi-clock"></i> {{ formatHora(consulta.horario_inicio) }}
                  </span>
                  <span v-if="consulta.valor" class="fw-bold text-dark ms-1">
                    R$ {{ consulta.valor }}
                  </span>
                </div>

                <div class="d-flex gap-2 align-items-center flex-wrap">
                  
                  <button
                    v-if="consulta.status === 'AGUARDANDO_PAGAMENTO'"
                    class="btn btn-warning btn-sm px-3 py-2 rounded-3 fw-semibold d-flex align-items-center gap-2"
                    @click="irParaPagamento(consulta.id)"
                  >
                    <i class="bi bi-credit-card"></i> Efetuar Pagamento
                  </button>

                  <button
                    v-if="consulta.status === 'CONFIRMADA' && consulta.link_video"
                    class="btn btn-enter btn-sm px-4 py-2 d-flex align-items-center gap-2"
                    @click="entrarConsulta(consulta)"
                  >
                    <i class="bi bi-camera-video-fill"></i> Entrar na Consulta
                  </button>

                  <div v-else-if="consulta.status === 'FINALIZADA'" class="concluded-actions">
                    <div class="rating mb-2 d-flex align-items-center gap-2">
                      <div class="stars text-warning small">
                        <i class="bi bi-star-fill" v-for="i in 5" :key="i"></i>
                      </div>
                      <small class="text-muted text-small">(Sua avaliação)</small>
                    </div>
                    <div class="d-flex gap-2">
                      <button class="btn btn-outline-secondary btn-sm d-flex align-items-center gap-2 px-3 py-2">
                        <i class="bi bi-file-earmark-text"></i> Ver Prescrição
                      </button>
                      <button class="btn btn-link btn-sm text-dark text-decoration-none d-flex align-items-center gap-2 text-small">
                        <i class="bi bi-download"></i> Baixar Atestado
                      </button>
                    </div>
                  </div>

                  <button
                    v-if="['CONFIRMADA', 'AGUARDANDO_PAGAMENTO'].includes(consulta.status)"
                    class="btn btn-outline-danger btn-sm px-3 py-2 rounded-3"
                    @click="cancelarConsulta(consulta.id)"
                  >
                    Cancelar Agendamento
                  </button>
                </div>
              </div>
            </div>

            <span class="status-badge" :class="statusBadgeClass(consulta.status)">
              {{ statusLabel(consulta.status) }}
            </span>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import SidebarPatientComp from '../../components/patient/SidebarPatientComp.vue'
import { consultaService } from '../../services/api.js'

const router = useRouter()
const loading = ref(true)
const consultas = ref([])
const activeTab = ref('TODAS')

// Mapeamento dinâmico das abas para cálculo correto dos contadores com dados da API
const tabs = computed(() => [
  { key: 'TODAS', label: 'Todas', count: consultas.value.length },
  { key: 'CONFIRMADA', label: 'Confirmadas', count: consultas.value.filter(c => c.status === 'CONFIRMADA').length },
  { key: 'AGUARDANDO_PAGAMENTO', label: 'Pendentes', count: consultas.value.filter(c => c.status === 'AGUARDANDO_PAGAMENTO').length },
  { key: 'FINALIZADA', label: 'Concluídas', count: consultas.value.filter(c => c.status === 'FINALIZADA').length },
  { key: 'CANCELADA', label: 'Canceladas', count: consultas.value.filter(c => c.status === 'CANCELADA').length },
])

const consultasFiltradas = computed(() => {
  if (activeTab.value === 'TODAS') return consultas.value
  return consultas.value.filter(c => c.status === activeTab.value)
})

const getInitials = (nome) => {
  if (!nome) return '?'
  return nome.split(' ').filter(n => n.length > 0).slice(0, 2).map(n => n[0]).join('')
}

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
    FINALIZADA: 'Concluída', 
    RESERVADA: 'Reservada' 
  }
  return map[s] || s
}

const statusBadgeClass = (s) => {
  if (s === 'CONFIRMADA') return 'confirmada'
  if (s === 'FINALIZADA') return 'concluida'
  if (s === 'CANCELADA') return 'cancelada'
  if (s === 'AGUARDANDO_PAGAMENTO') return 'pendente'
  return ''
}

const irParaPagamento = (id) => {
  router.push({ name: 'pagamento', query: { consultaId: id } })
}

const entrarConsulta = (consulta) => {
  router.push({ name: 'sala-teleconsulta', query: { consultaId: consulta.id, link: consulta.link_video } })
}

const cancelarConsulta = async (id) => {
  if (!confirm('Confirmar cancelamento da consulta?')) return
  try {
    await consultaService.cancelar(id)
    const res = await consultaService.listar()
    consultas.value = res.data
  } catch (e) {
    console.error(e)
    alert('Erro ao cancelar consulta')
  }
}

onMounted(async () => {
  try {
    const res = await consultaService.listar()
    consultas.value = res.data
  } catch (e) {
    console.error('Erro ao listar consultas da API:', e)
  } finally {
    loading.value = false
  }
})
</script>

<style scoped>
@import url("https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css");

.dashboard-wrapper { background-color: #f4f9f9; min-height: 100vh; }

/* Estrutura das Abas */
.tabs-container { display: flex; background-color: #e9eff2; padding: 5px; border-radius: 12px; gap: 4px; }
.tab-item { flex: 1; border: none; background: transparent; padding: 10px; font-weight: 500; color: #475569; border-radius: 10px; font-size: 0.85rem; transition: all 0.2s ease; }
.tab-item.active { background-color: white; color: #0468BF; box-shadow: 0 2px 8px rgba(0,0,0,0.05); font-weight: 600; }

/* Cards de Consulta */
.consult-card { background: white; border-radius: 20px; border: 1px solid #e2e8f0; transition: transform 0.2s, opacity 0.3s; }
.card-cancelled { opacity: 0.7; }

.avatar-circle { width: 60px; height: 60px; border-radius: 50%; background-color: #DFF2F0; color: #03A1E0; display: flex; align-items: center; justify-content: center; font-weight: bold; flex-shrink: 0; font-size: 1.2rem; }

.specialty-text { color: #03A1E0; font-weight: 500; }
.details { color: #64748b; font-size: 0.9rem; }

/* Botões Customizados */
.btn-enter { background-color: #0468BF; color: white; border: none; border-radius: 10px; padding: 10px 20px; font-weight: 600; transition: background 0.2s; }
.btn-enter:hover { background-color: #0060B4; color: white; }

.btn-outline-secondary { border: 1px solid #e2e8f0; background: white; color: #334155; font-weight: 500; border-radius: 10px; }
.btn-outline-secondary:hover { background-color: #f8fafc; }

.text-small { font-size: 0.8rem; }

/* Badges Laterais por Status */
.status-badge { padding: 6px 16px; border-radius: 20px; font-size: 0.75rem; font-weight: bold; white-space: nowrap; }
.status-badge.confirmada { background-color: #0468BF; color: white; }
.status-badge.concluida { background-color: #A3E4D7; color: #117A65; }
.status-badge.cancelada { background-color: transparent; border: 1px solid #CBD5E0; color: #64748B; }
.status-badge.pendente { background-color: #fef5ea; color: #f57c00; }
</style>