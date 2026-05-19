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
          />
        </div>
      </header>

      <div class="row g-3 mb-4">
        <div class="col-md-4">
          <div class="stat-card text-center py-4">
            <h2 class="fw-bold text-dark mb-0">2</h2>
            <p class="text-muted small mb-0">Agendadas</p>
          </div>
        </div>
        <div class="col-md-4">
          <div class="stat-card text-center py-4">
            <h2 class="fw-bold text-dark mb-0">4</h2>
            <p class="text-muted small mb-0">Finalizadas</p>
          </div>
        </div>
        <div class="col-md-4">
          <div class="stat-card text-center py-4">
            <h2 class="fw-bold text-dark mb-0">2</h2>
            <p class="text-muted small mb-0">Canceladas</p>
          </div>
        </div>
      </div>

      <div class="nav-pills-container p-1 mb-4 rounded-3 d-flex align-items-center bg-white shadow-sm border">
        <button class="btn-tab flex-grow-1 active">Todas (8)</button>
        <button class="btn-tab flex-grow-1">Agendadas (2)</button>
        <button class="btn-tab flex-grow-1">Finalizadas (4)</button>
        <button class="btn-tab flex-grow-1">Canceladas (2)</button>
      </div>

      <div class="d-flex flex-column gap-3">
        
        <div class="history-card p-4 bg-white rounded-4 border shadow-sm d-flex justify-content-between align-items-start">
          <div class="d-flex gap-3">
            <div class="initials-circle bg-blue-soft text-blue-deep fw-bold">MS</div>
            <div>
              <h5 class="fw-bold text-dark mb-1">Maria Silva</h5>
              <p class="text-muted small mb-2">Retorno</p>
              
              <div class="d-flex align-items-center gap-3 text-muted small mb-3">
                <span><i class="bi bi-calendar3 me-1"></i> 15 Mar 2026</span>
                <span><i class="bi bi-clock me-1"></i> 14:00</span>
                <span class="text-dark fw-medium">R$ 250,00</span>
              </div>

              <button class="btn btn-outline-secondary-custom btn-sm px-3 py-1.5 rounded-3 fw-semibold">
                <i class="bi bi-person me-1"></i> Ver Paciente
              </button>
            </div>
          </div>
          <span class="badge bg-primary-custom px-3 py-2 rounded-pill fw-semibold">Confirmada</span>
        </div>

        <div class="history-card p-4 bg-white rounded-4 border shadow-sm d-flex justify-content-between align-items-start">
          <div class="d-flex gap-3">
            <div class="initials-circle bg-blue-soft text-blue-deep fw-bold">JS</div>
            <div>
              <h5 class="fw-bold text-dark mb-1">João Santos</h5>
              <p class="text-muted small mb-2">Primeira consulta</p>
              
              <div class="d-flex align-items-center gap-3 text-muted small mb-3">
                <span><i class="bi bi-calendar3 me-1"></i> 15 Mar 2026</span>
                <span><i class="bi bi-clock me-1"></i> 10:30</span>
                <span class="text-dark fw-medium">R$ 300,00</span>
              </div>

              <button class="btn btn-outline-secondary-custom btn-sm px-3 py-1.5 rounded-3 fw-semibold">
                <i class="bi bi-person me-1"></i> Ver Paciente
              </button>
            </div>
          </div>
          <span class="badge bg-primary-custom px-3 py-2 rounded-pill fw-semibold">Confirmada</span>
        </div>

        <div class="history-card p-4 bg-white rounded-4 border shadow-sm d-flex justify-content-between align-items-start">
          <div class="d-flex gap-3">
            <div class="initials-circle bg-cyan-soft text-cyan-deep fw-bold">FC</div>
            <div>
              <h5 class="fw-bold text-dark mb-1">Fernanda Costa</h5>
              <p class="text-muted small mb-2">Retorno</p>
              
              <div class="d-flex align-items-center gap-3 text-muted small mb-3">
                <span><i class="bi bi-calendar3 me-1"></i> 12 Mar 2026</span>
                <span><i class="bi bi-clock me-1"></i> 16:00</span>
                <span class="text-dark fw-medium">R$ 250,00</span>
              </div>

              <button class="btn btn-outline-secondary-custom btn-sm px-3 py-1.5 rounded-3 fw-semibold">
                <i class="bi bi-person me-1"></i> Ver Paciente
              </button>
            </div>
          </div>
          <span class="badge bg-success-soft text-success px-3 py-2 rounded-pill fw-semibold">Finalizada</span>
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
</style>