<template>
  <div class="d-flex dashboard-wrapper">
    <SidebarPatientComp />

    <main class="content flex-grow-1 p-4">
      
      <div class="mb-4">
        <button class="btn btn-back d-flex align-items-center gap-2 text-muted fw-medium" @click="$router.back()">
          <i class="bi bi-arrow-left"></i> Voltar para lista de médicos
        </button>
      </div>

      <div class="section-card p-4 mb-4">
        <div class="d-flex justify-content-between align-items-start flex-wrap gap-3">
          <div class="d-flex gap-4 align-items-center">
            <div class="avatar-large bg-blue-soft text-primary-custom">DC</div>
            <div>
              <h4 class="fw-bold mb-1">Dr. Carlos Mendes</h4>
              <p class="text-info-custom fw-medium mb-2">Cardiologista</p>
              <p class="text-muted small mb-3 max-w-600">
                Especialista em cardiologia clínica e preventiva. Formado pela USP com residência no InCor.
              </p>
              <div class="d-flex gap-3 text-muted small">
                <span><i class="bi bi-star-fill text-warning me-1"></i> 4.9 (127)</span>
                <span><i class="bi bi-geo-alt me-1"></i> São Paulo, SP</span>
                <span><i class="bi bi-clock me-1"></i> 15 anos</span>
              </div>
            </div>
          </div>
          <div class="text-end">
            <small class="text-muted d-block">Valor da consulta</small>
            <h3 class="fw-bold text-dark">R$ 250,00</h3>
          </div>
        </div>
      </div>

      <div class="row g-4">
        <div class="col-lg-7">
          <div class="section-card p-4 h-100">
            <div class="d-flex justify-content-between align-items-center mb-4">
              <h6 class="fw-bold mb-0 d-flex align-items-center gap-2">
                <i class="bi bi-calendar3"></i> Selecione uma Data
              </h6>
              <div class="d-flex align-items-center gap-3">
                <button class="btn btn-icon-sm"><i class="bi bi-chevron-left"></i></button>
                <span class="fw-bold small">Abril 2026</span>
                <button class="btn btn-icon-sm"><i class="bi bi-chevron-right"></i></button>
              </div>
            </div>

            <div class="calendar-grid mb-2">
              <div class="day-label" v-for="d in ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb']" :key="d">{{ d }}</div>
            </div>

            <div class="calendar-grid">
              <div class="day-number empty" v-for="n in 3" :key="'empty-'+n"></div>
              <div class="day-number" 
                   v-for="n in 30" 
                   :key="n" 
                   :class="{ 'active': n === 16, 'disabled': n < 13 }">
                {{ n }}
              </div>
            </div>
          </div>
        </div>

        <div class="col-lg-5">
          <div class="section-card p-4 h-100">
            <h6 class="fw-bold mb-1 d-flex align-items-center gap-2">
              <i class="bi bi-clock"></i> Horários Disponíveis
            </h6>
            <p class="text-muted small mb-4">Horários para 16 de Abril de 2026</p>

            <div class="row g-2">
              <div class="col-6" v-for="hora in times" :key="hora.val">
                <button class="btn w-100 time-slot" :class="{ 'selected': hora.active, 'disabled': !hora.available }">
                  {{ hora.val }}
                </button>
              </div>
            </div>
            
            <button class="btn btn-primary-custom w-100 mt-4 py-2 fw-bold rounded-3">
              Confirmar Agendamento
            </button>
          </div>
        </div>
      </div>

    </main>
  </div>
</template>

<script setup>
import SidebarPatientComp from '../../components/patient/SidebarPatientComp.vue'

const times = [
  { val: '08:00', available: true, active: false },
  { val: '08:30', available: false, active: false },
  { val: '09:00', available: false, active: false },
  { val: '09:30', available: false, active: false },
  { val: '10:00', available: true, active: false },
  { val: '10:30', available: false, active: false },
  { val: '11:00', available: true, active: false },
  { val: '11:30', available: true, active: false },
  { val: '14:00', available: false, active: false },
  { val: '14:30', available: false, active: false },
  { val: '15:00', available: false, active: false },
  { val: '15:30', available: true, active: false },
  { val: '16:00', available: true, active: true }, // Exemplo selecionado
  { val: '16:30', available: true, active: false },
  { val: '17:00', available: true, active: false },
  { val: '17:30', available: false, active: false },
]
</script>

<style scoped>
.dashboard-wrapper {
  background: #F8FAFC;
  min-height: 100vh;
}

.section-card {
  background: white;
  border-radius: 16px;
  border: 1px solid #E2E8F0;
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
}

.bg-blue-soft { background: #EBF5FF; color: #3182CE; }
.text-info-custom { color: #00A09D; }
.max-w-600 { max-width: 600px; }

.calendar-grid {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  gap: 8px;
  text-align: center;
}

.day-label {
  font-size: 0.8rem;
  color: #94A3B8;
  font-weight: 500;
  padding-bottom: 10px;
}

.day-number {
  height: 45px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 10px;
  cursor: pointer;
  font-size: 0.9rem;
  transition: all 0.2s;
}

.day-number:hover:not(.disabled):not(.empty) {
  background: #f1f5f9;
}

.day-number.active {
  background: #0081B4;
  color: white;
  font-weight: bold;
}

.day-number.disabled {
  color: #CBD5E0;
  cursor: not-allowed;
}

.time-slot {
  border: 1px solid #E2E8F0;
  background: white;
  font-size: 0.85rem;
  font-weight: 500;
  padding: 10px;
  border-radius: 8px;
  color: #1a202c;
}

.time-slot.selected {
  background: #EBF5FF;
  border-color: #0081B4;
  color: #0081B4;
}

.time-slot.disabled {
  background: #F8FAFC;
  color: #CBD5E0;
  border-color: #EDF2F7;
  cursor: not-allowed;
}

.btn-icon-sm {
  background: #F1F5F9;
  border: none;
  width: 32px;
  height: 32px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.8rem;
}

.btn-back {
  border: none;
  background: none;
  padding: 0;
  font-size: 0.9rem;
}

.btn-primary-custom {
  background-color: #00A09D;
  border: none;
  color: white;
}
</style>