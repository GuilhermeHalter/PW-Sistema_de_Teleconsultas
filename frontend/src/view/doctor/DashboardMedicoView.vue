<template>
  <div class="d-flex dashboard-wrapper">
    <SidebarMedicoComp />

    <main class="content flex-grow-1 p-4">
      <header class="d-flex justify-content-between align-items-center mb-4">
        <div>
          <h3 class="fw-bold mb-1 text-dark">Olá, Dr. Carlos!</h3>
          <p class="text-muted">Bem-vindo ao seu painel de teleconsultas</p>
        </div>
      </header>

      <div class="row g-3 mb-5">
        <div class="col-md-3">
          <div class="stat-card blue-theme d-flex align-items-center gap-3">
            <div class="icon-box"><i class="bi bi-calendar-check"></i></div>
            <div>
              <h4 class="mb-0 fw-bold">4</h4>
              <p class="mb-0 text-muted small">Consultas Hoje</p>
            </div>
          </div>
        </div>
        <div class="col-md-3">
          <div class="stat-card cyan-theme d-flex align-items-center gap-3">
            <div class="icon-box"><i class="bi bi-people"></i></div>
            <div>
              <h4 class="mb-0 fw-bold">156</h4>
              <p class="mb-0 text-muted small">Pacientes Atendidos</p>
            </div>
          </div>
        </div>
        <div class="col-md-3">
          <div class="stat-card default-theme d-flex align-items-center gap-3">
            <div class="icon-box"><i class="bi bi-wallet2"></i></div>
            <div>
              <h4 class="mb-0 fw-bold">R$ 12.450</h4>
              <p class="mb-0 text-muted small">Receita do Mês</p>
            </div>
          </div>
        </div>
        <div class="col-md-3">
          <div class="stat-card default-theme d-flex align-items-center gap-3">
            <div class="icon-box"><i class="bi bi-graph-up-arrow"></i></div>
            <div>
              <h4 class="mb-0 fw-bold">+23%</h4>
              <p class="mb-0 text-muted small">Crescimento</p>
            </div>
          </div>
        </div>
      </div>

      <div class="row g-4">
        <div class="col-lg-8">
          <div class="section-card p-4 h-100">
            <div class="d-flex justify-content-between align-items-center mb-4">
              <h5 class="fw-bold mb-0">Consultas de Hoje (15 Mar 2026)</h5>
              <a href="#" class="text-decoration-none small text-secondary-custom">Ver agenda <i class="bi bi-chevron-right"></i></a>
            </div>

            <div class="consult-list d-flex flex-column gap-3">
              <div class="consult-item d-flex align-items-center justify-content-between p-3">
                <div class="d-flex align-items-center gap-3">
                  <div class="initials-circle bg-blue-soft text-blue-deep">09:00</div>
                  <div>
                    <h6 class="mb-0 fw-bold">Maria Silva</h6>
                    <small class="text-muted d-block">Retorno</small>
                    <small class="text-success-custom fw-semibold small"><i class="bi bi-check-circle-fill"></i> Confirmada</small>
                  </div>
                </div>
                <button class="btn btn-outline-primary-custom btn-sm px-3 fw-bold">
                  <i class="bi bi-camera-video-fill me-1"></i> Iniciar
                </button>
              </div>

              <div class="consult-item d-flex align-items-center justify-content-between p-3">
                <div class="d-flex align-items-center gap-3">
                  <div class="initials-circle bg-blue-soft text-blue-deep">10:30</div>
                  <div>
                    <h6 class="mb-0 fw-bold">João Santos</h6>
                    <small class="text-muted d-block">Primeira consulta</small>
                    <small class="text-success-custom fw-semibold small"><i class="bi bi-check-circle-fill"></i> Confirmada</small>
                  </div>
                </div>
                <button class="btn btn-outline-primary-custom btn-sm px-3 fw-bold">
                  <i class="bi bi-camera-video-fill me-1"></i> Iniciar
                </button>
              </div>

              <div class="consult-item d-flex align-items-center justify-content-between p-3">
                <div class="d-flex align-items-center gap-3">
                  <div class="initials-circle bg-cyan-soft text-cyan-deep">14:00</div>
                  <div>
                    <h6 class="mb-0 fw-bold">Ana Beatriz</h6>
                    <small class="text-muted d-block">Retorno</small>
                    <small class="text-warning-custom fw-semibold small"><i class="bi bi-exclamation-circle-fill"></i> Aguardando Pagamento</small>
                  </div>
                </div>
                <button class="btn btn-outline-secondary btn-sm px-3 fw-bold" disabled>
                  <i class="bi bi-camera-video-off-fill me-1"></i> Pendente
                </button>
              </div>

              <div class="consult-item d-flex align-items-center justify-content-between p-3">
                <div class="d-flex align-items-center gap-3">
                  <div class="initials-circle bg-blue-soft text-blue-deep">15:30</div>
                  <div>
                    <h6 class="mb-0 fw-bold">Pedro Oliveira</h6>
                    <small class="text-muted d-block">Primeira consulta</small>
                    <small class="text-success-custom fw-semibold small"><i class="bi bi-check-circle-fill"></i> Confirmada</small>
                  </div>
                </div>
                <button class="btn btn-outline-primary-custom btn-sm px-3 fw-bold">
                  <i class="bi bi-camera-video-fill me-1"></i> Iniciar
                </button>
              </div>
            </div>
          </div>
        </div>

        <div class="col-lg-4">
          <div class="section-card p-4 h-100">
            <div class="d-flex justify-content-between align-items-center mb-4">
              <h5 class="fw-bold mb-0"><i class="bi bi-bell me-2 text-warning"></i>Notificações</h5>
              <span class="badge rounded-pill bg-blue-deep">3</span>
            </div>

            <div class="notification-list d-flex flex-column gap-3">
              <div class="notification-item p-3 active-notify">
                <p class="mb-1 small fw-medium">Nova consulta agendada: Ana Beatriz - 15 Mar às 14:00</p>
                <small class="text-muted" style="font-size: 0.75rem;">30min atrás</small>
              </div>
              <div class="notification-item p-3">
                <p class="mb-1 small fw-medium">Pagamento confirmado: João Santos - Consulta de 15 Mar</p>
                <small class="text-muted" style="font-size: 0.75rem;">1h atrás</small>
              </div>
              <div class="notification-item p-3">
                <p class="mb-1 small fw-medium">Consulta cancelada: Lucas Ferreira - 17 Mar às 10:00</p>
                <small class="text-muted" style="font-size: 0.75rem;">2h atrás</small>
              </div>
            </div>
          </div>
        </div>

        <div class="col-12 mt-2">
          <div class="section-card p-4">
            <div class="d-flex justify-content-between align-items-center mb-4">
              <h5 class="fw-bold mb-0">Próximas Consultas</h5>
              <a href="#" class="text-decoration-none small text-secondary-custom">Ver todas <i class="bi bi-chevron-right"></i></a>
            </div>
            <div class="row g-3">
              <div class="col-md-6">
                <div class="consult-item d-flex align-items-center gap-3 p-3">
                  <div class="initials-circle bg-light text-muted">CM</div>
                  <div class="flex-grow-1">
                    <h6 class="mb-0 fw-bold">Carla Mendes</h6>
                    <small class="text-muted d-block"><i class="bi bi-calendar3 me-1"></i> 16 Mar 2026 <i class="bi bi-clock ms-2 me-1"></i> 09:00</small>
                  </div>
                </div>
              </div>
              <div class="col-md-6">
                <div class="consult-item d-flex align-items-center gap-3 p-3">
                  <div class="initials-circle bg-light text-muted">RL</div>
                  <div class="flex-grow-1">
                    <h6 class="mb-0 fw-bold">Roberto Lima</h6>
                    <small class="text-muted d-block"><i class="bi bi-calendar3 me-1"></i> 16 Mar 2026 <i class="bi bi-clock ms-2 me-1"></i> 11:00</small>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
import SidebarMedicoComp from '../../components/doctor/SidebarDoctorComp.vue';

export default {
  components: {
    SidebarMedicoComp
  }
}
</script>

<style scoped>
@import url("https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css");

/* Variáveis de Cores Exatas da sua Paleta */
:root {
  --color-1: #98DEF8;
  --color-2: #0468BF;
  --color-3: #0060B4;
  --color-4: #03A1E0;
  --color-5: #DFF2F0;
}

.dashboard-wrapper {
  background-color: #f0f7f7; /* Mesma variação leve do #DFF2F0 */
  min-height: 100vh;
  font-family: 'Inter', sans-serif;
}

/* Botões Customizados Originais */
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

/* Stat Cards e Temas Idênticos ao Original do Paciente */
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
  background: #03A1E0; /* Azul Céu */
  color: white;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.4rem;
}
.stat-card.blue-theme .icon-box { background-color: #0468BF; }

/* Section Cards */
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

/* Círculos com Iniciais / Horários */
.initials-circle {
  width: 54px;
  height: 54px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  font-size: 0.9rem;
}
.bg-blue-soft { background-color: #eef7ff; }
.text-blue-deep { color: #0468BF; }
.bg-cyan-soft { background-color: #DFF2F0; }
.text-cyan-deep { color: #0060B4; }

/* Notificações */
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

/* Pequenos utilitários de texto mantendo consistência */
.text-success-custom { color: #0468BF; }
.text-warning-custom { color: #f57c00; }
</style>