<template>
  <div class="d-flex dashboard-wrapper">
    <SidebarPatientComp />

    <main class="content flex-grow-1 p-4">
      <!-- Botão Voltar -->
      <div class="mb-4">
        <button class="btn btn-back d-flex align-items-center gap-2 fw-medium" @click="$router.back()">
          <i class="bi bi-arrow-left"></i> Voltar para lista de médicos
        </button>
      </div>

      <!-- Card de Perfil do Médico (Dinâmico) -->
      <div class="section-card p-4 mb-4">
        <div class="d-flex justify-content-between align-items-start flex-wrap gap-3">
          <div class="d-flex gap-4 align-items-center">
            <div class="avatar-large bg-cyan-soft text-blue-deep">
              {{ getInitials(medicoNome) }}
            </div>
            <div>
              <h4 class="fw-bold mb-1">{{ medicoNome }}</h4>
              <p class="text-azure fw-medium mb-0">Teleconsulta Online</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Spinner de Carregamento da API -->
      <div v-if="loading" class="text-center py-5">
        <div class="spinner-border text-primary" role="status"></div>
        <p class="text-muted mt-2">Carregando horários...</p>
      </div>

      <div v-else>
        <!-- Estado de Fallback: Sem Horários no Banco -->
        <div v-if="horarios.length === 0" class="text-center py-5 text-muted section-card p-4">
          <i class="bi bi-calendar-x fs-1 d-block mb-2 text-azure"></i>
          <h5 class="fw-bold text-dark">Nenhum horário disponível</h5>
          <p class="small mb-0">Este médico não possui horários disponíveis para agendamento no momento.</p>
        </div>

        <!-- Grade de Horários Disponíveis Reativa -->
        <div v-else class="section-card p-4">
          <h6 class="fw-bold mb-4 d-flex align-items-center gap-2 text-dark">
            <i class="bi bi-clock text-azure"></i> Horários Disponíveis
          </h6>

          <div class="row g-3 mb-4">
            <div 
              class="col-6 col-md-4 col-lg-3" 
              v-for="horario in horarios" 
              :key="horario.id"
            >
              <button
                class="btn w-100 time-slot"
                :class="{ 'selected': horarioSelecionado?.id === horario.id }"
                @click="selecionarHorario(horario)"
              >
                <span class="d-block fw-bold text-capitalize">
                  {{ formatData(horario.data_hora_inicio) }}
                </span>
                <span class="d-block small text-muted mt-1">
                  {{ formatHora(horario.data_hora_inicio) }}
                </span>
              </button>
            </div>
          </div>

          <!-- Resumo Informativo do Horário Selecionado -->
          <div v-if="horarioSelecionado" class="selected-summary p-3 rounded-3 mb-4 animate-fade-in">
            <p class="mb-0 small fw-semibold text-blue-deep">
              <i class="bi bi-check-circle-fill me-2"></i>
              Horário selecionado: <span class="text-capitalize">{{ formatData(horarioSelecionado.data_hora_inicio) }}</span> às {{ formatHora(horarioSelecionado.data_hora_inicio) }}
            </p>
          </div>

          <!-- Alerta de Retorno de Erros da API -->
          <div v-if="erro" class="alert alert-danger py-2 small mb-4 d-flex align-items-center gap-2">
            <i class="bi bi-exclamation-triangle-fill"></i> {{ erro }}
          </div>

          <!-- Botão de Ação de Agendamento -->
          <button
            class="btn btn-primary-custom w-100 py-3 fw-bold rounded-3 shadow-sm"
            :disabled="!horarioSelecionado || agendando"
            @click="confirmarAgendamento"
          >
            <span v-if="agendando" class="spinner-border spinner-border-sm me-2" role="status"></span>
            <i v-else class="bi bi-calendar-check me-2"></i>
            Confirmar Agendamento
          </button>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import SidebarPatientComp from '../../components/patient/SidebarPatientComp.vue'
import { horarioService, consultaService } from '../../services/api.js'

const route = useRoute()
const router = useRouter()

// Estados de controle reativo
const loading = ref(true)
const agendando = ref(false)
const horarios = ref([])
const horarioSelecionado = ref(null)
const erro = ref('')

// Captura dos parâmetros passados pela rota da lista de médicos
const medicoId = route.query.medicoId
const medicoNome = route.query.medicoNome || 'Médico'

const getInitials = (nome) => {
  if (!nome) return '?'
  return nome.split(' ').filter(n => n.length > 0).slice(0, 2).map(n => n[0]).join('')
}

const formatData = (iso) => {
  if (!iso) return '-'
  return new Date(iso).toLocaleDateString('pt-BR', { weekday: 'short', day: '2-digit', month: 'short' })
}

const formatHora = (iso) => {
  if (!iso) return '-'
  const d = new Date(iso)
  return `${String(d.getHours()).padStart(2, '0')}:${String(d.getMinutes()).padStart(2, '0')}`
}

const selecionarHorario = (horario) => {
  horarioSelecionado.value = horarioSelecionado.value?.id === horario.id ? null : horario
}

const confirmarAgendamento = async () => {
  if (!horarioSelecionado.value || !medicoId) return
  erro.value = ''
  agendando.value = true
  
  try {
    // Criação da consulta passando payload esperado pelo Django
    const res = await consultaService.criar({
      medico: medicoId,
      horario: horarioSelecionado.value.id
    })
    // Redirecionamento com o id da nova consulta para a tela de pagamento
    router.push({ name: 'pagamento', query: { consultaId: res.data.id } })
  } catch (e) {
    console.error(e)
    erro.value = e.response?.data?.error || 'Erro ao agendar consulta. Tente novamente.'
  } finally {
    agendando.value = false
  }
}

onMounted(async () => {
  // Redireciona de volta caso a tela seja acessada sem um médico alvo definido
  if (!medicoId) {
    router.push({ name: 'agendamento' })
    return
  }
  
  try {
    const res = await horarioService.listarDisponiveis(medicoId)
    horarios.value = res.data
  } catch (e) {
    console.error('Erro ao sincronizar horários do médico:', e)
  } finally {
    loading.value = false
  }
})
</script>

<style scoped>
@import url("https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css");

.dashboard-wrapper { 
  background-color: #f4f9f9; 
  min-height: 100vh; 
}

/* Cards e Layout */
.section-card { 
  background: white; 
  border-radius: 20px; 
  border: 1px solid #e2e8f0; 
  box-shadow: 0 4px 6px -1px rgba(0,0,0,0.02); 
}

.avatar-large { 
  width: 80px; 
  height: 80px; 
  border-radius: 50%; 
  display: flex; 
  align-items: center; 
  justify-content: center; 
  font-size: 1.5rem; 
  font-weight: bold; 
  flex-shrink: 0;
}

.bg-cyan-soft { background-color: #DFF2F0; } 
.text-blue-deep { color: #0468BF; }
.text-azure { color: #03A1E0; }

/* Slots de Horários */
.time-slot { 
  border: 1px solid #e2e8f0; 
  background: white; 
  font-size: 0.85rem; 
  font-weight: 600; 
  padding: 12px 8px; 
  border-radius: 12px; 
  color: #475569; 
  transition: all 0.2s ease; 
}
.time-slot:hover:not(.selected) { 
  border-color: #03A1E0; 
  background-color: #f0faff; 
}
.time-slot.selected { 
  background-color: #DFF2F0; 
  border-color: #0468BF; 
  color: #0468BF; 
}

/* Feedback de Seleção */
.selected-summary { 
  background-color: #eef7ff; 
  border: 1px solid #98DEF8; 
  animation: fadeIn 0.2s ease-out;
}

/* Botões */
.btn-primary-custom { 
  background-color: #0468BF; 
  border: none; 
  color: white; 
  transition: background-color 0.2s; 
}
.btn-primary-custom:hover:not(:disabled) { 
  background-color: #0060B4; 
}
.btn-primary-custom:disabled { 
  background-color: #94a3b8; 
  cursor: not-allowed;
}

.btn-back { 
  border: none; 
  background: none; 
  padding: 0; 
  font-size: 0.9rem; 
  color: #03A1E0; 
  transition: color 0.2s;
}
.btn-back:hover { 
  color: #0060B4; 
}

/* Animação Simples */
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(-5px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>