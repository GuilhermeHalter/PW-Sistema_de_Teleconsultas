<template>
  <div class="d-flex dashboard-wrapper">
    <SidebarPatientComp />

    <main class="content flex-grow-1 p-4">
      <!-- Header do Painel -->
      <header class="d-flex justify-content-between align-items-center mb-4">
        <div>
          <h3 class="fw-bold mb-1 text-dark">Olá, {{ nomeUsuario }}!</h3>
          <p class="text-muted">Bem-vinda ao seu painel de teleconsultas</p>
        </div>
      </header>

      <!-- Grid de Estatísticas Reativo -->
      <div class="row g-3 mb-5">
        <div class="col-md-3">
          <div class="stat-card blue-theme d-flex align-items-center gap-3">
            <div class="icon-box"><i class="bi bi-calendar-check"></i></div>
            <div>
              <h4 class="mb-0 fw-bold">{{ loading ? '...' : proximasConsultas.length }}</h4>
              <p class="mb-0 text-muted small">Próximas Consultas</p>
            </div>
          </div>
        </div>
        <div class="col-md-3">
          <div class="stat-card cyan-theme d-flex align-items-center gap-3">
            <div class="icon-box"><i class="bi bi-clock"></i></div>
            <div>
              <h4 class="mb-0 fw-bold">{{ loading ? '...' : totalRealizadas }}</h4>
              <p class="mb-0 text-muted small">Consultas Realizadas</p>
            </div>
          </div>
        </div>
        <div class="col-md-3">
          <div class="stat-card default-theme d-flex align-items-center gap-3">
            <div class="icon-box"><i class="bi bi-camera-video"></i></div>
            <div>
              <h4 class="mb-0 fw-bold">{{ loading ? '...' : tempoMedio }}</h4>
              <p class="mb-0 text-muted small">Tempo Médio</p>
            </div>
          </div>
        </div>
        <div class="col-md-3">
          <div class="stat-card default-theme d-flex align-items-center gap-3">
            <div class="icon-box"><i class="bi bi-star"></i></div>
            <div>
              <h4 class="mb-0 fw-bold">{{ loading ? '...' : avaliacaoMedia }}</h4>
              <p class="mb-0 text-muted small">Avaliação Média</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Spinner Centralizado de Carregamento -->
      <div v-if="loading" class="text-center py-5">
        <div class="spinner-border text-primary" role="status"></div>
        <p class="text-muted mt-2">Sincronizando painel do paciente...</p>
      </div>

      <div v-else class="row g-4">
        <!-- Coluna da Esquerda: Próximas Consultas Dinâmicas -->
        <div class="col-lg-8">
          <div class="section-card p-4 h-100">
            <div class="d-flex justify-content-between align-items-center mb-4">
              <h5 class="fw-bold mb-0">Próximas Consultas</h5>
              <a href="#" class="text-decoration-none small text-secondary-custom">Ver todas <i class="bi bi-chevron-right"></i></a>
            </div>

            <div class="consult-list d-flex flex-column gap-3">
              <!-- Renderização baseada em dados reais -->
              <div 
                v-for="(consult, index) in proximasConsultas" 
                :key="consult.id" 
                class="consult-item d-flex align-items-center justify-content-between p-3"
              >
                <div class="d-flex align-items-center gap-3">
                  <div 
                    class="initials-circle" 
                    :class="index % 2 === 0 ? 'bg-blue-soft text-blue-deep' : 'bg-cyan-soft text-cyan-deep'"
                  >
                    {{ getInitials(consult.medicoNome || consult.medico?.nomeCompleto) }}
                  </div>
                  <div>
                    <h6 class="mb-0 fw-bold">{{ consult.medicoNome || consult.medico?.nomeCompleto }}</h6>
                    <small class="text-muted d-block">
                      {{ consult.especialidade || consult.medico?.especialidades_detalhes?.map(e => e.nome).join(', ') || 'Especialista' }}
                    </small>
                    <small class="text-muted">
                      <i class="bi bi-calendar3 me-1"></i> {{ consult.data_formatada || consult.data }}
                      <i class="bi bi-clock ms-2 me-1"></i> {{ consult.hora }}
                    </small>
                  </div>
                </div>
                
                <router-link 
                  :to="{ name: 'sala-teleconsulta', params: { id: consult.id } }"
                  class="btn btn-outline-primary-custom btn-sm px-3 fw-bold text-decoration-none"
                >
                  <i class="bi bi-camera-video-fill me-1"></i> Entrar
                </router-link>
              </div>

              <!-- Estado caso não possua nenhuma consulta agendada no banco -->
              <div v-if="proximasConsultas.length === 0" class="text-center py-5 text-muted small">
                <i class="bi bi-calendar-x d-block mb-2 fs-3 text-secondary-custom"></i>
                Você não tem nenhuma teleconsulta agendada no momento.
              </div>
            </div>
          </div>
        </div>

        <!-- Coluna da Direita: Notificações Dinâmicas -->
        <div class="col-lg-4">
          <div class="section-card p-4 h-100">
            <div class="d-flex justify-content-between align-items-center mb-4">
              <h5 class="fw-bold mb-0"><i class="bi bi-bell me-2 text-warning"></i>Notificações</h5>
              <span class="badge rounded-pill bg-blue-deep">{{ notificacoes.length }}</span>
            </div>

            <div class="notification-list d-flex flex-column gap-3">
              <div 
                v-for="notif in notificacoes" 
                :key="notif.id" 
                class="notification-item p-3"
                :class="{ 'active-notify': notif.lida === false }"
              >
                <p class="mb-1 small fw-medium">{{ notif.texto }}</p>
                <small class="text-muted" style="font-size: 0.75rem;">{{ notif.tempo }}</small>
              </div>

              <div v-if="notificacoes.length === 0" class="text-center py-4 text-muted small">
                Não há novas notificações.
              </div>
            </div>
          </div>
        </div>

        <!-- Linha Inferior: Histórico / Consultas Passadas -->
        <div class="col-12 mt-2">
          <div class="section-card p-4">
            <div class="d-flex justify-content-between align-items-center mb-4">
              <h5 class="fw-bold mb-0">Consultas Passadas</h5>
              <a href="#" class="text-decoration-none small text-secondary-custom">Ver histórico completo <i class="bi bi-chevron-right"></i></a>
            </div>
            
            <div class="row g-3">
              <div 
                v-for="historico in consultasPassadas" 
                :key="historico.id" 
                class="col-md-6"
              >
                <div class="consult-item d-flex align-items-center gap-3 p-3">
                  <div class="initials-circle bg-light text-muted">
                    {{ getInitials(historico.medicoNome) }}
                  </div>
                  <div class="flex-grow-1">
                    <h6 class="mb-0 fw-bold">{{ historico.medicoNome }}</h6>
                    <small class="text-muted d-block">{{ historico.especialidade }}</small>
                    <small class="text-muted">{{ historico.data }}</small>
                  </div>
                  <span class="badge rounded-pill bg-light text-dark border">Concluída</span>
                </div>
              </div>

              <div v-if="consultasPassadas.length === 0" class="col-12 text-center py-4 text-muted small">
                Nenhuma consulta anterior registrada.
              </div>
            </div>

          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import SidebarPatientComp from '../../components/patient/SidebarPatientComp.vue'
// Exemplo de importação de serviço de consultas ou perfil, mude de acordo com a sua estrutura:
// import { consultaService } from '../../services/api.js'

// Controle de Estado de carregamento
const loading = ref(true)

// Dados do Usuário Logado
const nomeUsuario = ref('Maria') // Pode ser preenchido dinamicamente via Auth/Vuex/Pinia

// Variáveis reativas das Estatísticas prontas para receberem sua API
const totalRealizadas = ref(0)
const tempoMedio = ref('0min')
const avaliacaoMedia = ref('0.0')

// Arrays que receberão as respostas das requisições reais do seu banco
const proximasConsultas = ref([])
const consultasPassadas = ref([])
const notificacoes = ref([])

const getInitials = (nome) => {
  if (!nome) return '?'
  return nome.split(' ').filter(n => n.length > 0).slice(0, 2).map(n => n[0]).join('')
}

onMounted(async () => {
  try {
    // Insira aqui as chamadas reais para preencher as variáveis do seu painel, Exemplo:
    // const resConsultas = await consultaService.listarDoPaciente()
    // proximasConsultas.value = resConsultas.data.agendadas
    // consultasPassadas.value = resConsultas.data.historico
    // totalRealizadas.value = resConsultas.data.totalRealizadas
    
    // Simulação temporária de requisição finalizada com arrays vazios
    proximasConsultas.value = []
    consultasPassadas.value = []
    notificacoes.value = []
  } catch (e) {
    console.error('Erro ao buscar dados do painel do paciente:', e)
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

.btn-outline-primary-custom {
  border: 1px solid #0468BF;
  color: #0468BF;
  background: transparent;
}
.btn-outline-primary-custom:hover {
  background: #0468BF;
  color: white;
}

.stat-card {
  padding: 20px;
  border-radius: 16px;
  border: 1px solid #E2E8F0;
  background: white;
  transition: transform 0.2s;
}
.stat-card:hover { transform: translateY(-3px); }

.stat-card.blue-theme { background-color: #eef7ff; border-color: #98DEF8; }
.stat-card.cyan-theme { background-color: #DFF2F0; border-color: #b8e2de; }

.stat-card .icon-box {
  width: 48px;
  height: 48px;
  background: #03A1E0;
  color: white;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.4rem;
}
.stat-card.blue-theme .icon-box { background-color: #0468BF; }

.section-card {
  background: white;
  border-radius: 16px;
  border: 1px solid #E2E8F0;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
}

.consult-item {
  border: 1px solid #f1f5f9;
  background-color: #ffffff;
  border-radius: 12px;
  transition: all 0.2s;
}
.consult-item:hover { border-color: #98DEF8; background-color: #fcfdfe; }

.initials-circle {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
}
.bg-blue-soft { background-color: #eef7ff; }
.text-blue-deep { color: #0468BF; }
.bg-cyan-soft { background-color: #DFF2F0; }
.text-cyan-deep { color: #0060B4; }

.notification-item {
  background-color: #f8fafc;
  border-radius: 10px;
  border-left: 4px solid transparent;
}
.active-notify {
  border-left-color: #03A1E0;
  background-color: #f0f9ff;
}

.bg-blue-deep { background-color: #0468BF; }
.text-secondary-custom { color: #03A1E0; font-weight: 600; }
</style>