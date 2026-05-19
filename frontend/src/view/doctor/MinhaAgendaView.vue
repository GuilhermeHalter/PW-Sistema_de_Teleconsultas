<template>
  <div class="d-flex dashboard-wrapper">
    <SidebarMedicoComp />

    <main class="content flex-grow-1 p-4">
      <header class="mb-4">
        <h3 class="fw-bold mb-1 text-dark">Minha Agenda</h3>
        <p class="text-muted">Visualize e gerencie suas consultas agendadas</p>
      </header>

      <div class="section-card p-3 mb-4 d-flex justify-content-between align-items-center">
        <button class="btn btn-link text-dark p-0"><i class="bi bi-chevron-left fs-5"></i></button>
        <div class="text-center">
          <h5 class="fw-bold mb-0 text-dark">Domingo, 15 de Março de 2026</h5>
          <small class="text-muted">3 confirmadas | 1 pendentes</small>
        </div>
        <button class="btn btn-link text-dark p-0"><i class="bi bi-chevron-right fs-5"></i></button>
      </div>

      <div class="d-flex flex-column gap-3">
        
        <div class="consult-item-expanded d-flex align-items-center justify-content-between p-4 shadow-sm bg-white">
          <div class="d-flex align-items-center gap-4">
            <div class="time-container text-center">
              <span class="time-hour fw-bold d-block">09</span>
              <span class="time-minutes text-muted">:00</span>
            </div>
            <div>
              <h5 class="mb-1 fw-bold text-dark">Maria Silva</h5>
              <p class="mb-1 text-muted small">Retorno</p>
              <span class="text-dark fw-medium small">R$ 250,00</span>
            </div>
          </div>
          <div class="d-flex align-items-center gap-3">
            <span class="badge bg-success-soft text-success px-3 py-2 rounded-pill fw-semibold">Confirmada</span>
            <button class="btn btn-primary-custom px-4 py-2 rounded-3 fw-bold shadow-sm d-flex align-items-center gap-2">
              <i class="bi bi-camera-video-fill"></i> Iniciar
            </button>
          </div>
        </div>

        <div class="consult-item-expanded d-flex align-items-center justify-content-between p-4 shadow-sm bg-white">
          <div class="d-flex align-items-center gap-4">
            <div class="time-container text-center">
              <span class="time-hour fw-bold d-block">10</span>
              <span class="time-minutes text-muted">:30</span>
            </div>
            <div>
              <h5 class="mb-1 fw-bold text-dark">João Santos</h5>
              <p class="mb-1 text-muted small">Primeira consulta</p>
              <span class="text-dark fw-medium small">R$ 300,00</span>
            </div>
          </div>
          <div class="d-flex align-items-center gap-3">
            <span class="badge bg-success-soft text-success px-3 py-2 rounded-pill fw-semibold">Confirmada</span>
            <button class="btn btn-primary-custom px-4 py-2 rounded-3 fw-bold shadow-sm d-flex align-items-center gap-2">
              <i class="bi bi-camera-video-fill"></i> Iniciar
            </button>
          </div>
        </div>

        <div class="consult-item-expanded d-flex align-items-center justify-content-between p-4 shadow-sm bg-white">
          <div class="d-flex align-items-center gap-4">
            <div class="time-container text-center">
              <span class="time-hour fw-bold d-block">14</span>
              <span class="time-minutes text-muted">:00</span>
            </div>
            <div>
              <h5 class="mb-1 fw-bold text-dark">Ana Beatriz</h5>
              <p class="mb-1 text-muted small">Retorno</p>
              <span class="text-dark fw-medium small">R$ 250,00</span>
            </div>
          </div>
          <div class="d-flex align-items-center gap-3">
            <span class="badge bg-warning-soft text-warning px-3 py-2 rounded-pill fw-semibold">Aguardando Pagamento</span>
            </div>
        </div>

        <div class="consult-item-expanded d-flex align-items-center justify-content-between p-4 shadow-sm bg-white">
          <div class="d-flex align-items-center gap-4">
            <div class="time-container text-center">
              <span class="time-hour fw-bold d-block">15</span>
              <span class="time-minutes text-muted">:30</span>
            </div>
            <div>
              <h5 class="mb-1 fw-bold text-dark">Pedro Oliveira</h5>
              <p class="mb-1 text-muted small">Primeira consulta</p>
              <span class="text-dark fw-medium small">R$ 300,00</span>
            </div>
          </div>
          <div class="d-flex align-items-center gap-3">
            <span class="badge bg-success-soft text-success px-3 py-2 rounded-pill fw-semibold">Confirmada</span>
            <button class="btn btn-primary-custom px-4 py-2 rounded-3 fw-bold shadow-sm d-flex align-items-center gap-2">
              <i class="bi bi-camera-video-fill"></i> Iniciar
            </button>
          </div>
        </div>

      </div>
    </main>
  </div>
</template>

<script setup>
import SidebarMedicoComp from '../../components/doctor/SidebarDoctorComp.vue';
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