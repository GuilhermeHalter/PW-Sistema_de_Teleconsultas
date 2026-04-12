<template>
  <div class="d-flex dashboard-wrapper">
    <SidebarPatientComp />

    <main class="content flex-grow-1 p-4">
      <div class="mb-4">
        <h3 class="fw-bold text-dark">Encontre seu Médico</h3>
        <p class="text-muted">Escolha um especialista e agende sua teleconsulta</p>
      </div>

      <div class="d-flex gap-3 mb-4 align-items-center">
        <div class="flex-grow-1 position-relative">
          <i class="bi bi-search search-icon"></i>
          <input
            type="text"
            class="form-control custom-input ps-5 py-2"
            placeholder="Buscar por nome ou especialidade..."
          />
        </div>

        <div class="d-flex gap-2">
           <button class="btn btn-filter"><i class="bi bi-filter"></i></button>
           <select class="form-select custom-select">
            <option>Todas</option>
            <option>Cardiologia</option>
            <option>Dermatologia</option>
            <option>Pediatria</option>
          </select>
        </div>
      </div>

      <p class="text-muted small mb-3">{{ doctors.length }} médico(s) encontrado(s)</p>

      <div class="row g-4">
        <div class="col-md-6 col-lg-4" v-for="doc in doctors" :key="doc.name">
          <div class="doctor-card h-100 shadow-sm">
            <div class="p-4 d-flex gap-3 align-items-start position-relative">
              <div class="avatar-circle" :class="doc.initialsColor">
                {{ doc.initials }}
              </div>

              <div class="flex-grow-1">
                <h6 class="fw-bold mb-0 text-dark">{{ doc.name }}</h6>
                <div class="text-info-custom fw-medium small">{{ doc.specialty }}</div>

                <div class="small mt-1">
                  <span class="text-warning"><i class="bi bi-star-fill"></i> {{ doc.rating }}</span>
                  <span class="text-muted ms-1">({{ doc.reviews }} avaliações)</span>
                </div>

                <div class="small text-muted mt-2">
                  <i class="bi bi-geo-alt"></i> {{ doc.city }}
                </div>

                <div class="small text-muted mt-1">
                  {{ doc.exp }} anos de experiência
                </div>
              </div>

              <span 
                class="badge status-badge"
                :class="doc.available ? 'badge-available' : 'badge-unavailable'"
              >
                {{ doc.available ? 'Disponível' : 'Indisponível' }}
              </span>
            </div>

            <div class="card-footer-custom d-flex justify-content-between align-items-center p-4">
              <div>
                <div class="text-muted x-small">Consulta a partir de</div>
                <div class="fw-bold price-text">R$ {{ doc.price }}</div>
              </div>

              <button class="btn btn-teal btn-sm px-3 py-2 d-flex align-items-center gap-2">
                <router-link to="/horarios-consulta" class="text-white text-decoration-none">
                  <i class="bi bi-calendar-event-fill"></i> Agendar
                </router-link>
              </button>

            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import SidebarPatientComp from '../../components/patient/SidebarPatientComp.vue'

const doctors = [
  { name: 'Dr. Carlos Mendes', specialty: 'Cardiologista', rating: 4.9, reviews: 127, city: 'São Paulo, SP', exp: 15, price: '250.00', initials: 'DC', available: true, initialsColor: 'bg-blue-soft' },
  { name: 'Dra. Ana Beatriz', specialty: 'Dermatologista', rating: 4.8, reviews: 98, city: 'Rio de Janeiro, RJ', exp: 12, price: '200.00', initials: 'DA', available: true, initialsColor: 'bg-teal-soft' },
  { name: 'Dr. Paulo Roberto', specialty: 'Clínico Geral', rating: 4.7, reviews: 215, city: 'Belo Horizonte, MG', exp: 20, price: '150.00', initials: 'DP', available: true, initialsColor: 'bg-blue-soft' },
  { name: 'Dra. Fernanda Lima', specialty: 'Nutricionista', rating: 4.9, reviews: 76, city: 'Curitiba, PR', exp: 8, price: '180.00', initials: 'DF', available: false, initialsColor: 'bg-blue-soft' },
  { name: 'Dr. Ricardo Santos', specialty: 'Psiquiatra', rating: 4.8, reviews: 142, city: 'Porto Alegre, RS', exp: 18, price: '300.00', initials: 'DR', available: true, initialsColor: 'bg-blue-soft' },
  { name: 'Dra. Mariana Costa', specialty: 'Pediatra', rating: 5, reviews: 189, city: 'Salvador, BA', exp: 10, price: '180.00', initials: 'DM', available: true, initialsColor: 'bg-blue-soft' }
]
</script>

<style scoped>
.dashboard-wrapper {
  background: #f1f5f9;
  min-height: 100vh;
}

.custom-input, .custom-select {
  border-radius: 12px;
  border: 1px solid #e2e8f0;
}

.search-icon {
  position: absolute;
  left: 15px;
  top: 50%;
  transform: translateY(-50%);
  color: #94a3b8;
}

.btn-filter {
  background: white;
  border: 1px solid #e2e8f0;
  border-radius: 10px;
  padding: 8px 12px;
  color: #64748b;
}

.doctor-card {
  background: white;
  border-radius: 16px;
  border: 1px solid #eef2f6;
  transition: transform 0.2s;
}

.avatar-circle {
  width: 52px;
  height: 52px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 1.1rem;
}

.bg-blue-soft { background: #EBF5FF; color: #3182CE; }
.bg-teal-soft { background: #E6FFFA; color: #319795; }

.status-badge {
  font-size: 0.7rem;
  padding: 5px 10px;
  border-radius: 20px;
  position: absolute;
  right: 20px;
  top: 50%;
  transform: translateY(-100%);
}

.badge-available { background: #E6F6EC; color: #22C55E; }
.badge-unavailable { background: #F1F5F9; color: #64748B; border: 1px solid #E2E8F0; }

.card-footer-custom {
  border-top: 1px solid #f1f5f9;
}

.price-text { font-size: 1.25rem; color: #1a202c; }
.x-small { font-size: 0.75rem; }
.text-info-custom { color: #00A09D; }

.btn-teal {
  background: #0081B4; 
  color: white;
  border-radius: 10px;
  font-weight: 600;
  border: none;
}

.btn-teal:hover {
  background: #006b96;
}
</style>