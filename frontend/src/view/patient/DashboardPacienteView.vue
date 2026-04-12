<template>
  <div class="d-flex dashboard-wrapper">

    <SidebarPatientComp />

    <main class="content flex-grow-1 p-4">
      <header class="d-flex justify-content-between align-items-center mb-4">
        <div>
          <h3 class="fw-bold mb-1">Olá, Maria!</h3>
          <p class="text-muted">Bem-vinda ao seu painel de teleconsultas</p>
        </div>
        <button class="btn btn-primary-custom px-4 py-2 rounded-3 fw-bold">
          <i class="bi bi-plus-lg me-1"></i> Agendar Nova Consulta
        </button>
      </header>

      <div class="row g-3 mb-5">
        <div class="col-md-3">
          <div class="stat-card blue d-flex align-items-center gap-3">
            <div class="icon-box"><i class="bi bi-calendar-check"></i></div>
            <div>
              <h4 class="mb-0 fw-bold">2</h4>
              <p class="mb-0 text-muted small">Próximas Consultas</p>
            </div>
          </div>
        </div>
        <div class="col-md-3">
          <div class="stat-card green d-flex align-items-center gap-3">
            <div class="icon-box"><i class="bi bi-clock"></i></div>
            <div>
              <h4 class="mb-0 fw-bold">12</h4>
              <p class="mb-0 text-muted small">Consultas Realizadas</p>
            </div>
          </div>
        </div>
        <div class="col-md-3">
          <div class="stat-card light d-flex align-items-center gap-3">
            <div class="icon-box"><i class="bi bi-camera-video"></i></div>
            <div>
              <h4 class="mb-0 fw-bold">45min</h4>
              <p class="mb-0 text-muted small">Tempo Médio</p>
            </div>
          </div>
        </div>
        <div class="col-md-3">
          <div class="stat-card light d-flex align-items-center gap-3">
            <div class="icon-box"><i class="bi bi-star"></i></div>
            <div>
              <h4 class="mb-0 fw-bold">4.9</h4>
              <p class="mb-0 text-muted small">Avaliação Média</p>
            </div>
          </div>
        </div>
      </div>

      <div class="row g-4">
        <div class="col-lg-8">
          <div class="section-card p-4 h-100">
            <div class="d-flex justify-content-between align-items-center mb-4">
              <h5 class="fw-bold mb-0">Próximas Consultas</h5>
              <a href="#" class="text-decoration-none text-muted small">Ver todas <i class="bi bi-chevron-right"></i></a>
            </div>

            <div class="consult-list d-flex flex-column gap-3">
              <div class="consult-item d-flex align-items-center justify-content-between p-3">
                <div class="d-flex align-items-center gap-3">
                  <div class="initials-circle">DC</div>
                  <div>
                    <h6 class="mb-0 fw-bold">Dr. Carlos Mendes</h6>
                    <small class="text-muted d-block">Cardiologista</small>
                    <small class="text-muted"><i class="bi bi-calendar3 me-1"></i> 15 Mar 2026 <i class="bi bi-clock ms-2 me-1"></i> 14:00</small>
                  </div>
                </div>
                <button class="btn btn-outline-primary-custom btn-sm px-3">
                  <i class="bi bi-camera-video-fill me-1"></i> Entrar
                </button>
              </div>
              <div class="consult-item d-flex align-items-center justify-content-between p-3">
                <div class="d-flex align-items-center gap-3">
                  <div class="initials-circle blue">DA</div>
                  <div>
                    <h6 class="mb-0 fw-bold">Dra. Ana Beatriz</h6>
                    <small class="text-muted d-block">Dermatologista</small>
                    <small class="text-muted"><i class="bi bi-calendar3 me-1"></i> 18 Mar 2026 <i class="bi bi-clock ms-2 me-1"></i> 10:30</small>
                  </div>
                </div>
                <button class="btn btn-outline-primary-custom btn-sm px-3">
                  <i class="bi bi-camera-video-fill me-1"></i> Entrar
                </button>
              </div>
            </div>
          </div>
        </div>

        <div class="col-lg-4">
          <div class="section-card p-4 h-100">
            <div class="d-flex justify-content-between align-items-center mb-4">
              <h5 class="fw-bold mb-0"><i class="bi bi-bell me-2"></i>Notificações</h5>
              <span class="badge rounded-pill bg-success-subtle text-success">2</span>
            </div>

            <div class="notification-list d-flex flex-column gap-3">
              <div class="notification-item p-3">
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

        <div class="col-12 mt-2">
          <div class="section-card p-4">
            <div class="d-flex justify-content-between align-items-center mb-4">
              <h5 class="fw-bold mb-0">Consultas Passadas</h5>
              <a href="#" class="text-decoration-none text-muted small">Ver histórico completo <i class="bi bi-chevron-right"></i></a>
            </div>
            <div class="row g-3">
              <div class="col-md-6">
                <div class="consult-item d-flex align-items-center gap-3 p-3">
                  <div class="initials-circle gray">DP</div>
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
                  <div class="initials-circle gray">DF</div>
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

.dashboard-wrapper {
  background-color: #F8FAFC;
  min-height: 100vh;
  font-family: 'Inter', sans-serif;
}

.sidebar {
  width: 260px;
  background: white;
  border-right: 1px solid #E2E8F0;
  height: 100vh;
  position: sticky;
  top: 0;
}

.logo-icon {
  width: 35px;
  height: 35px;
  font-size: 1.2rem;
}

.nav-link {
  color: #64748B;
  font-weight: 500;
  padding: 10px 15px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  gap: 12px;
}

.nav-link.active {
  background-color: #00A09D;
  color: white;
}

.nav-link:hover:not(.active) {
  background-color: #F1F5F9;
}

.user-profile {
  background-color: #E6F3F3;
}

.avatar {
  width: 35px;
  height: 35px;
}

.stat-card {
  padding: 20px;
  border-radius: 16px;
  border: 1px solid #E2E8F0;
  background: white;
}

.stat-card.blue { background-color: #EBF5FF; border-color: #D1E9FF; }
.stat-card.green { background-color: #E6F3F3; border-color: #C6E7E7; }

.stat-card .icon-box {
  width: 48px;
  height: 48px;
  background: #00A09D;
  color: white;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.4rem;
}

.stat-card.blue .icon-box { background-color: #0077B6; }

.section-card {
  background: white;
  border-radius: 16px;
  border: 1px solid #E2E8F0;
}

.consult-item {
  border: 1px solid #E2E8F0;
  border-radius: 12px;
}

.initials-circle {
  width: 50px;
  height: 50px;
  background: #EBF5FF;
  color: #0077B6;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
}

.initials-circle.blue { background: #E0F2F1; color: #00897B; }
.initials-circle.gray { background: #F1F5F9; color: #64748B; }

.notification-item {
  background-color: #F8FAFC;
  border-radius: 10px;
  border-left: 4px solid transparent;
}
.notification-item:first-child { border-left-color: #00A09D; }

.btn-primary-custom {
  background-color: #00A09D;
  border: none;
  color: white;
}

.btn-outline-primary-custom {
  border: 1px solid #00A09D;
  color: #00A09D;
  background: transparent;
}

.btn-outline-primary-custom:hover {
  background: #00A09D;
  color: white;
}
</style>