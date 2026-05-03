<template>
  <div class="d-flex dashboard-wrapper">
    <SidebarPatientComp />

    <main class="content flex-grow-1 p-4">
      <header class="d-flex justify-content-between align-items-center mb-4">
        <div>
          <h3 class="fw-bold mb-1 text-dark">Olá, Maria!</h3>
          <p class="text-muted">Bem-vinda ao seu painel de teleconsultas</p>
        </div>
        <!-- Botão com o Azul de Destaque -->
        <button class="btn btn-primary-custom px-4 py-2 rounded-3 fw-bold shadow-sm">
          <i class="bi bi-plus-lg me-1"></i> Agendar Nova Consulta
        </button>
      </header>

      <div class="row g-3 mb-5">
        <!-- Stat Card: Próximas -->
        <div class="col-md-3">
          <div class="stat-card blue-theme d-flex align-items-center gap-3">
            <div class="icon-box"><i class="bi bi-calendar-check"></i></div>
            <div>
              <h4 class="mb-0 fw-bold">2</h4>
              <p class="mb-0 text-muted small">Próximas Consultas</p>
            </div>
          </div>
        </div>
        <!-- Stat Card: Realizadas -->
        <div class="col-md-3">
          <div class="stat-card cyan-theme d-flex align-items-center gap-3">
            <div class="icon-box"><i class="bi bi-clock"></i></div>
            <div>
              <h4 class="mb-0 fw-bold">12</h4>
              <p class="mb-0 text-muted small">Consultas Realizadas</p>
            </div>
          </div>
        </div>
        <!-- Stat Card: Tempo -->
        <div class="col-md-3">
          <div class="stat-card default-theme d-flex align-items-center gap-3">
            <div class="icon-box"><i class="bi bi-camera-video"></i></div>
            <div>
              <h4 class="mb-0 fw-bold">45min</h4>
              <p class="mb-0 text-muted small">Tempo Médio</p>
            </div>
          </div>
        </div>
        <!-- Stat Card: Avaliação -->
        <div class="col-md-3">
          <div class="stat-card default-theme d-flex align-items-center gap-3">
            <div class="icon-box"><i class="bi bi-star"></i></div>
            <div>
              <h4 class="mb-0 fw-bold">4.9</h4>
              <p class="mb-0 text-muted small">Avaliação Média</p>
            </div>
          </div>
        </div>
      </div>

      <div class="row g-4">
        <!-- Próximas Consultas -->
        <div class="col-lg-8">
          <div class="section-card p-4 h-100">
            <div class="d-flex justify-content-between align-items-center mb-4">
              <h5 class="fw-bold mb-0">Próximas Consultas</h5>
              <a href="#" class="text-decoration-none small text-secondary-custom">Ver todas <i class="bi bi-chevron-right"></i></a>
            </div>

            <div class="consult-list d-flex flex-column gap-3">
              <div class="consult-item d-flex align-items-center justify-content-between p-3">
                <div class="d-flex align-items-center gap-3">
                  <div class="initials-circle bg-blue-soft text-blue-deep">CM</div>
                  <div>
                    <h6 class="mb-0 fw-bold">Dr. Carlos Mendes</h6>
                    <small class="text-muted d-block">Cardiologista</small>
                    <small class="text-muted"><i class="bi bi-calendar3 me-1"></i> 15 Mar 2026 <i class="bi bi-clock ms-2 me-1"></i> 14:00</small>
                  </div>
                </div>
                <button class="btn btn-outline-primary-custom btn-sm px-3 fw-bold">
                  <i class="bi bi-camera-video-fill me-1"></i> Entrar
                </button>
              </div>
              
              <div class="consult-item d-flex align-items-center justify-content-between p-3">
                <div class="d-flex align-items-center gap-3">
                  <div class="initials-circle bg-cyan-soft text-cyan-deep">AB</div>
                  <div>
                    <h6 class="mb-0 fw-bold">Dra. Ana Beatriz</h6>
                    <small class="text-muted d-block">Dermatologista</small>
                    <small class="text-muted"><i class="bi bi-calendar3 me-1"></i> 18 Mar 2026 <i class="bi bi-clock ms-2 me-1"></i> 10:30</small>
                  </div>
                </div>
                <button class="btn btn-outline-primary-custom btn-sm px-3 fw-bold">
                  <i class="bi bi-camera-video-fill me-1"></i> Entrar
                </button>
              </div>
            </div>
          </div>
        </div>

        <!-- Notificações -->
        <div class="col-lg-4">
          <div class="section-card p-4 h-100">
            <div class="d-flex justify-content-between align-items-center mb-4">
              <h5 class="fw-bold mb-0"><i class="bi bi-bell me-2 text-warning"></i>Notificações</h5>
              <span class="badge rounded-pill bg-blue-deep">2</span>
            </div>

            <div class="notification-list d-flex flex-column gap-3">
              <div class="notification-item p-3 active-notify">
                <p class="mb-1 small fw-medium">Sua consulta com Dr. Carlos Mendes está confirmada para amanhã.</p>
                <small class="text-muted" style="font-size: 0.75rem;">2h atrás</small>
              </div>
              <div class="notification-item p-3">
                <p class="mb-1 small fw-medium">Não esqueça de preencher o questionário pré-consulta.</p>
                <small class="text-muted" style="font-size: 0.75rem;">1 dia atrás</small>
              </div>
            </div>
          </div>
        </div>

        <!-- Consultas Passadas -->
        <div class="col-12 mt-2">
          <div class="section-card p-4">
            <div class="d-flex justify-content-between align-items-center mb-4">
              <h5 class="fw-bold mb-0">Consultas Passadas</h5>
              <a href="#" class="text-decoration-none small text-secondary-custom">Ver histórico completo <i class="bi bi-chevron-right"></i></a>
            </div>
            <div class="row g-3">
              <div class="col-md-6">
                <div class="consult-item d-flex align-items-center gap-3 p-3">
                  <div class="initials-circle bg-light text-muted">PR</div>
                  <div class="flex-grow-1">
                    <h6 class="mb-0 fw-bold">Dr. Paulo Roberto</h6>
                    <small class="text-muted d-block">Clínico Geral</small>
                    <small class="text-muted">02 Mar 2026</small>
                  </div>
                  <span class="badge rounded-pill bg-light text-dark border">Concluída</span>
                </div>
              </div>
              <div class="col-md-6">
                <div class="consult-item d-flex align-items-center gap-3 p-3">
                  <div class="initials-circle bg-light text-muted">FL</div>
                  <div class="flex-grow-1">
                    <h6 class="mb-0 fw-bold">Dra. Fernanda Lima</h6>
                    <small class="text-muted d-block">Nutricionista</small>
                    <small class="text-muted">25 Fev 2026</small>
                  </div>
                  <span class="badge rounded-pill bg-light text-dark border">Concluída</span>
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
import SidebarPatientComp from '../../components/patient/SidebarPatientComp.vue';

export default {
  components: {
    SidebarPatientComp
  }
}
</script>

<style scoped>
@import url("https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css");

/* Variáveis de Cores Baseadas na sua Paleta */
:root {
  --color-1: #98DEF8;
  --color-2: #0468BF;
  --color-3: #0060B4;
  --color-4: #03A1E0;
  --color-5: #DFF2F0;
}

.dashboard-wrapper {
  background-color: #f0f7f7; /* Variação leve do #DFF2F0 para o fundo */
  min-height: 100vh;
  font-family: 'Inter', sans-serif;
}

/* Botões Customizados */
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

/* Stat Cards */
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

/* Círculos com Iniciais */
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
</style>