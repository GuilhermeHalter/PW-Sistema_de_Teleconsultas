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
            v-model="busca"
          />
        </div>

        <div class="d-flex gap-2">
           <button class="btn btn-filter"><i class="bi bi-filter"></i></button>
           <select class="form-select custom-select" v-model="especialidadeSelecionada">
            <option value="">Todas as especialidades</option>
            <option v-for="esp in listaEspecialidades" :key="esp" :value="esp">
              {{ esp }}
            </option>
          </select>
        </div>
      </div>

      <div v-if="loading" class="text-center py-5">
        <div class="spinner-border text-primary" role="status"></div>
        <p class="text-muted mt-2">Carregando médicos...</p>
      </div>

      <div v-else>
        <p class="text-muted small mb-3">{{ medicosFiltrados.length }} médico(s) encontrado(s)</p>

        <div v-if="medicosFiltrados.length === 0" class="text-center py-5 text-muted">
          <i class="bi bi-person-x fs-1 d-block mb-2"></i>
          Nenhum médico encontrado para os critérios selecionados.
        </div>

        <div v-else class="row g-4">
          <div class="col-md-6 col-lg-4" v-for="doc in medicosFiltrados" :key="doc.id">
            <div class="doctor-card h-100 shadow-sm">
              <div class="p-4 d-flex gap-3 align-items-start position-relative">
                
                <div class="avatar-circle" :class="doc.disponivel !== false ? 'bg-cyan-light text-blue-deep' : 'bg-gray-light text-muted'">
                  {{ getInitials(doc.nomeCompleto) }}
                </div>

                <div class="flex-grow-1">
                  <h6 class="fw-bold mb-0 text-dark">{{ doc.nomeCompleto }}</h6>
                  <div class="text-azure fw-medium small">
                    {{ doc.especialidades_detalhes?.map(e => e.nome).join(', ') || 'Clínica Geral' }}
                  </div>

                  <div class="small mt-1">
                    <span class="text-warning"><i class="bi bi-star-fill"></i> {{ doc.rating || '4.8' }}</span>
                    <span class="text-muted ms-1">({{ doc.reviews || '94' }} avaliações)</span>
                  </div>

                  <div class="small text-muted mt-2">
                    <i class="bi bi-geo-alt"></i> {{ doc.cidade || 'Telemedicina' }}
                  </div>

                  <div class="small text-muted mt-1">
                    {{ doc.experiencia || '10' }} anos de experiência
                  </div>
                  
                  <div class="small text-muted mt-1">CRM: {{ doc.crm }}</div>
                </div>

                <span 
                  class="badge status-badge"
                  :class="doc.disponivel !== false ? 'badge-available' : 'badge-unavailable'"
                >
                  {{ doc.disponivel !== false ? 'Disponível' : 'Indisponível' }}
                </span>
              </div>

              <div class="card-footer-custom d-flex justify-content-between align-items-center p-4">
                <div>
                  <div class="text-muted x-small">Consulta online</div>
                  <div class="fw-bold price-text">
                    {{ doc.preco ? `R$ ${doc.preco}` : 'Online' }}
                  </div>
                </div>

                <router-link 
                  :to="{ name: 'horarios-consulta', query: { medicoId: doc.id, medicoNome: doc.nomeCompleto } }" 
                  class="btn btn-action btn-sm px-3 py-2 d-flex align-items-center gap-2 text-decoration-none"
                >
                  <i class="bi bi-calendar-event-fill"></i> Agendar
                </router-link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import SidebarPatientComp from '../../components/patient/SidebarPatientComp.vue'
import { medicoService } from '../../services/api.js'

const loading = ref(true)
const medicos = ref([])
const busca = ref('')
const especialidadeSelecionada = ref('')

// Mapeamento dinâmico de especialidades vindas do banco para alimentar o select do 1º código
const listaEspecialidades = computed(() => {
  const espSet = new Set()
  medicos.value.forEach(m => {
    m.especialidades_detalhes?.forEach(e => {
      if (e.nome) espSet.add(e.nome)
    })
  })
  return Array.from(espSet).sort()
})

// Motor de filtro integrado combinando Input Text e Select Box
const medicosFiltrados = computed(() => {
  return medicos.value.filter(m => {
    const correspondeBusca = !busca.value || 
      m.nomeCompleto?.toLowerCase().includes(busca.value.toLowerCase()) ||
      m.especialidades_detalhes?.some(e => e.nome?.toLowerCase().includes(busca.value.toLowerCase()))

    const correspondeEspecialidade = !especialidadeSelecionada.value ||
      m.especialidades_detalhes?.some(e => e.nome === especialidadeSelecionada.value)

    return correspondeBusca && correspondeEspecialidade
  })
})

const getInitials = (nome) => {
  if (!nome) return '?'
  return nome.split(' ').filter(n => n.length > 0).slice(0, 2).map(n => n[0]).join('')
}

onMounted(async () => {
  try {
    const res = await medicoService.listar()
    medicos.value = Array.isArray(res.data) ? res.data : (res.data?.dados || [])
  } catch (e) {
    console.error('Erro ao buscar lista de médicos da API:', e)
  } finally {
    loading.value = false
  }
})
</script>

<style scoped>
@import url("https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css");

.dashboard-wrapper {
  background-color: #f4f9f9;
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
  color: white;
}
</style>