<template>
  <div class="d-flex dashboard-wrapper">
    <SidebarMedicoComp />

    <main class="content flex-grow-1 p-4">
      <header class="d-flex justify-content-between align-items-center mb-4">
        <div>
          <h3 class="fw-bold mb-1 text-dark">Gerenciar Horários</h3>
          <p class="text-muted">Configure seus dias e horários disponíveis para atendimento</p>
        </div>
        <div class="d-flex align-items-center gap-3">
          <div class="input-group input-group-sm shadow-sm rounded-3 overflow-hidden border">
            <span class="input-group-text bg-white border-0 text-muted"><i class="bi bi-clock"></i></span>
            <span class="input-group-text bg-white border-0 fw-bold small pe-1">Duração:</span>
            <select class="form-select border-0 fw-bold text-primary-custom" style="width: 100px;">
              <option>30 min</option>
              <option>45 min</option>
              <option>60 min</option>
            </select>
          </div>
          <button class="btn btn-primary-custom px-4 py-2 rounded-3 fw-bold shadow-sm d-flex align-items-center gap-2">
            <i class="bi bi-save"></i> Salvar
          </button>
        </div>
      </header>

      <div class="row g-4 mb-4">
        <div class="col-md-6 col-lg-3">
          <div class="stat-card p-3 d-flex align-items-center gap-3 bg-white">
            <div class="icon-box-round bg-blue-soft text-blue-deep"><i class="bi bi- stopwatch"></i></div>
            <div>
              <h5 class="mb-0 fw-bold">30 min</h5>
              <p class="mb-0 text-muted small">Por consulta</p>
            </div>
          </div>
        </div>
        <div class="col-md-6 col-lg-3">
          <div class="stat-card p-3 d-flex align-items-center gap-3 bg-white">
            <div class="icon-box-round bg-cyan-soft text-cyan-deep"><i class="bi bi-calendar-range"></i></div>
            <div>
              <h5 class="mb-0 fw-bold">5 dias</h5>
              <p class="mb-0 text-muted small">Ativos por semana</p>
            </div>
          </div>
        </div>
        <div class="col-md-6 col-lg-3">
          <div class="stat-card p-3 d-flex align-items-center gap-3 bg-white border-dashed">
            <div class="icon-box-round bg-light text-muted"><i class="bi bi-plus-lg"></i></div>
            <div>
              <h5 class="mb-0 fw-bold">90</h5>
              <p class="mb-0 text-muted small">Slots semanais</p>
            </div>
          </div>
        </div>
      </div>

      <div class="row g-4">
        <div class="col-lg-6">
          <div class="section-card p-4 h-100 bg-white shadow-sm border">
            <div class="d-flex justify-content-between align-items-center mb-4">
              <h5 class="fw-bold mb-0"><i class="bi bi-calendar3 me-2"></i>Selecione uma Data</h5>
              <div class="calendar-nav d-flex align-items-center gap-3">
                <button class="btn btn-sm btn-light rounded-circle"><i class="bi bi-chevron-left"></i></button>
                <span class="fw-bold text-dark">Maio 2026</span>
                <button class="btn btn-sm btn-light rounded-circle"><i class="bi bi-chevron-right"></i></button>
              </div>
            </div>

            <div class="calendar-grid">
              <div class="weekday">Dom</div><div class="weekday">Seg</div><div class="weekday">Ter</div>
              <div class="weekday">Qua</div><div class="weekday">Qui</div><div class="weekday">Sex</div><div class="weekday">Sáb</div>
              
              <div class="day empty"></div><div class="day empty"></div><div class="day empty"></div>
              <div class="day empty"></div><div class="day empty"></div><div class="day">1</div><div class="day">2</div>
              <div class="day">3</div><div class="day">4</div><div class="day">5</div><div class="day">6</div><div class="day">7</div>
              <div class="day active">8</div><div class="day">9</div>
              <div class="day">10</div><div class="day has-slots">11</div><div class="day has-slots">12</div>
              <div class="day has-slots">13</div><div class="day has-slots">14</div><div class="day has-slots">15</div><div class="day">16</div>
              <div class="day">17</div><div class="day has-slots">18</div><div class="day has-slots">19</div>
              <div class="day has-slots">20</div><div class="day has-slots">21</div><div class="day has-slots">22</div><div class="day">23</div>
              <div class="day">24</div><div class="day has-slots">25</div><div class="day has-slots">26</div>
              <div class="day has-slots">27</div><div class="day has-slots">28</div><div class="day has-slots">29</div><div class="day">30</div>
            </div>
          </div>
        </div>

        <div class="col-lg-6">
          <div class="section-card p-4 h-100 bg-white shadow-sm border">
            <div class="d-flex justify-content-between align-items-center mb-4">
              <div>
                <h5 class="fw-bold mb-1 text-dark"><i class="bi bi-clock-history me-2"></i>Horários Disponíveis</h5>
                <p class="text-muted small mb-0">Horários para 8 de Maio de 2026</p>
              </div>
              <div class="d-flex align-items-center gap-2">
                <span class="small fw-bold text-muted">Sexta</span>
                <div class="form-check form-switch fs-5 p-0 m-0 ms-2">
                  <input class="form-check-input custom-switch m-0" type="checkbox" checked>
                </div>
              </div>
            </div>

            <div class="slots-grid">
              <div v-for="slot in slots" :key="slot.time" class="slot-item" :class="{ 'active': slot.active }">
                {{ slot.time }}
              </div>
              <button class="btn-add-slot">
                <i class="bi bi-plus-lg me-1"></i> Adicionar
              </button>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import SidebarMedicoComp from '../../components/doctor/SidebarDoctorComp.vue';

const slots = ref([
  { time: '08:00', active: true }, { time: '08:30', active: true }, { time: '09:00', active: true },
  { time: '09:30', active: true }, { time: '10:00', active: true }, { time: '10:30', active: true },
  { time: '11:00', active: true }, { time: '11:30', active: true }, { time: '13:00', active: true },
  { time: '13:30', active: true }, { time: '14:00', active: true }, { time: '14:30', active: true },
  { time: '15:00', active: true }, { time: '15:30', active: true }, { time: '16:00', active: true },
  { time: '16:30', active: true }, { time: '17:00', active: true }, { time: '17:30', active: true }
])
</script>

<style scoped>
@import url("https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css");

.dashboard-wrapper {
  background-color: #f0f7f7;
  min-height: 100vh;
  font-family: 'Inter', sans-serif;
}

.stat-card {
  border-radius: 16px;
  border: 1px solid #e2e8f0;
}
.icon-box-round {
  width: 42px;
  height: 42px;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.2rem;
}
.border-dashed { border-style: dashed !important; }

.calendar-grid {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  gap: 10px;
  text-align: center;
}
.weekday {
  font-weight: bold;
  color: #94a3b8;
  font-size: 0.85rem;
  padding-bottom: 10px;
}
.day {
  aspect-ratio: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  cursor: pointer;
  font-weight: 500;
  color: #475569;
  font-size: 0.95rem;
  position: relative;
  transition: all 0.2s;
}
.day:hover:not(.empty) { background-color: #f1f5f9; }
.day.active {
  background-color: #0468BF;
  color: white;
  font-weight: bold;
  box-shadow: 0 4px 8px rgba(4, 104, 191, 0.3);
}
.day.has-slots::after {
  content: '';
  position: absolute;
  bottom: 5px;
  width: 4px;
  height: 4px;
  background-color: #0468BF;
  border-radius: 50%;
}

.slots-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 12px;
}
.slot-item {
  padding: 10px;
  text-align: center;
  border-radius: 8px;
  background-color: #f8fafc;
  border: 1px solid #e2e8f0;
  font-weight: 600;
  color: #64748b;
  font-size: 0.9rem;
  cursor: pointer;
  transition: all 0.2s;
}
.slot-item.active {
  background-color: #e6f6f4;
  border-color: #2ec4b6;
  color: #2e7d32;
}
.slot-item:hover {
  transform: translateY(-2px);
  border-color: #0468BF;
}

.btn-add-slot {
  border: 2px dashed #cbd5e1;
  background: transparent;
  border-radius: 8px;
  color: #64748b;
  font-weight: 600;
  font-size: 0.9rem;
  transition: all 0.2s;
}
.btn-add-slot:hover {
  border-color: #0468BF;
  color: #0468BF;
  background-color: #eef7ff;
}

.custom-switch:checked {
  background-color: #0468BF;
  border-color: #0468BF;
}

.text-primary-custom { color: #0468BF; }
.bg-blue-soft { background-color: #eef7ff; }
.text-blue-deep { color: #0468BF; }
.bg-cyan-soft { background-color: #DFF2F0; }
.text-cyan-deep { color: #0060B4; }

@media (max-width: 1400px) {
  .slots-grid { grid-template-columns: repeat(3, 1fr); }
}
</style>