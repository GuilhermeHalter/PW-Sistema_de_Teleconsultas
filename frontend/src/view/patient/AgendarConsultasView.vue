<template>
  <div class="d-flex dashboard-wrapper">
    <SidebarPatientComp />

    <main class="content flex-grow-1 p-4">
      <div class="mb-4">
        <h3 class="fw-bold text-dark">Encontre seu Médico</h3>
        <p class="text-muted">Escolha um especialista e agende sua teleconsulta</p>
      </div>

      <!-- Barra de Busca e Filtros -->
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
            <option>Todas as especialidades</option>
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
              <!-- Avatar com cores da paleta -->
              <div class="avatar-circle" :class="doc.available ? 'bg-cyan-light text-blue-deep' : 'bg-gray-light text-muted'">
                {{ doc.initials }}
              </div>

              <div class="flex-grow-1">
                <h6 class="fw-bold mb-0 text-dark">{{ doc.name }}</h6>
                <div class="text-azure fw-medium small">{{ doc.specialty }}</div>

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

              <!-- Badge de Disponibilidade -->
              <span 
                class="badge status-badge"
                :class="doc.available ? 'badge-available' : 'badge-unavailable'"
              >
                {{ doc.available ? 'Disponível' : 'Indisponível' }}
              </span>
            </div>

            <!-- Rodapé do Card com Preço e Botão -->
            <div class="card-footer-custom d-flex justify-content-between align-items-center p-4">
              <div>
                <div class="text-muted x-small">Consulta a partir de</div>
                <div class="fw-bold price-text">R$ {{ doc.price }}</div>
              </div>

              <router-link to="/horarios-consulta" class="btn btn-action btn-sm px-3 py-2 d-flex align-items-center gap-2 text-decoration-none">
                <i class="bi bi-calendar-event-fill"></i> Agendar
              </router-link>
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
  { name: 'Dr. Carlos Mendes', specialty: 'Cardiologista', rating: 4.9, reviews: 127, city: 'São Paulo, SP', exp: 15, price: '250.00', initials: 'DC', available: true },
  { name: 'Dra. Ana Beatriz', specialty: 'Dermatologista', rating: 4.8, reviews: 98, city: 'Rio de Janeiro, RJ', exp: 12, price: '200.00', initials: 'DA', available: true },
  { name: 'Dr. Paulo Roberto', specialty: 'Clínico Geral', rating: 4.7, reviews: 215, city: 'Belo Horizonte, MG', exp: 20, price: '150.00', initials: 'DP', available: true },
  { name: 'Dra. Fernanda Lima', specialty: 'Nutricionista', rating: 4.9, reviews: 76, city: 'Curitiba, PR', exp: 8, price: '180.00', initials: 'DF', available: false },
  { name: 'Dr. Ricardo Santos', specialty: 'Psiquiatra', rating: 4.8, reviews: 142, city: 'Porto Alegre, RS', exp: 18, price: '300.00', initials: 'DR', available: true },
  { name: 'Dra. Mariana Costa', specialty: 'Pediatra', rating: 5, reviews: 189, city: 'Salvador, BA', exp: 10, price: '180.00', initials: 'DM', available: true }
]
</script>

<style scoped>
/* Cores da Paleta: #98DEF8, #0468BF, #0060B4, #03A1E0, #DFF2F0 */

.dashboard-wrapper {
  background-color: #f4f9f9; /* Variação do #DFF2F0 */
  min-height: 100vh;
}

/* Input e Seleção */
.custom-input, .custom-select {
  border-radius: 12px;
  border: 1px solid #c5e5e2;
  transition: all 0.2s;
}

.custom-input:focus, .custom-select:focus {
  border-color: #03A1E0;
  box-shadow: 0 0 0 0.25rem rgba(3, 161, 224, 0.1);
}

.search-icon {
  position: absolute;
  left: 15px;
  top: 50%;
  transform: translateY(-50%);
  color: #03A1E0;
}

.btn-filter {
  background: white;
  border: 1px solid #c5e5e2;
  border-radius: 10px;
  padding: 8px 12px;
  color: #0468BF;
}

.btn-filter:hover {
  background-color: #DFF2F0;
}

/* Cards dos Médicos */
.doctor-card {
  background: white;
  border-radius: 20px;
  border: 1px solid #e2e8f0;
  transition: transform 0.2s, box-shadow 0.2s;
}

.doctor-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 15px -3px rgba(4, 104, 191, 0.1) !important;
}

/* Avatar e Cores */
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

.bg-cyan-light { background-color: #DFF2F0; }
.text-blue-deep { color: #0468BF; }
.bg-gray-light { background-color: #f1f5f9; }
.text-azure { color: #03A1E0; }

/* Badges */
.status-badge {
  font-size: 0.7rem;
  padding: 5px 10px;
  border-radius: 20px;
  position: absolute;
  right: 20px;
  top: 20px;
}

.badge-available { 
  background-color: #e6f6ec; 
  color: #22c55e; 
}
.badge-unavailable { 
  background-color: #f1f5f9; 
  color: #64748b; 
  border: 1px solid #e2e8f0; 
}

/* Rodapé do Card */
.card-footer-custom {
  border-top: 1px solid #f1f5f9;
  background-color: #fafdfd;
  border-bottom-left-radius: 20px;
  border-bottom-right-radius: 20px;
}

.price-text { 
  font-size: 1.25rem; 
  color: #0060B4; 
}

.x-small { font-size: 0.75rem; }

/* Botão de Ação Principal */
.btn-action {
  background-color: #0468BF;
  color: white;
  border-radius: 12px;
  font-weight: 600;
  border: none;
  transition: all 0.2s;
}

.btn-action:hover {
  background-color: #0060B4;
  transform: scale(1.05);
  color: white;
}
</style>