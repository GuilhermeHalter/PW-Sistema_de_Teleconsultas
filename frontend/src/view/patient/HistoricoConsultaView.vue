<template>
  <div class="dashboard-wrapper d-flex">
    <SidebarPatientComp />

    <main class="content flex-grow-1 p-4">
      <header class="mb-4">
        <h3 class="fw-bold text-dark mb-1">Histórico de Consultas</h3>
        <p class="text-muted">Visualize todas as suas consultas passadas e futuras</p>
      </header>

      <div class="tabs-container mb-5">
        <button
          v-for="tab in tabs"
          :key="tab.label"
          :class="['tab-item', activeTab === tab.label ? 'active' : '']"
          @click="activeTab = tab.label"
        >
          {{ tab.label }} ({{ tab.count }})
        </button>
      </div>

      <div class="consult-list d-flex flex-column gap-4">
        <div
          v-for="consulta in filteredConsultas"
          :key="consulta.id"
          class="consult-card p-4"
          :class="{ 'card-cancelled': consulta.status === 'Cancelada' }"
        >
          <div class="d-flex justify-content-between align-items-start">
            <div class="d-flex gap-4">
              <div class="avatar-circle">
                {{ getInitials(consulta.nome) }}
              </div>

              <div class="info">
                <h5 class="fw-bold text-dark mb-1">{{ consulta.nome }}</h5>
                <p class="specialty-text mb-3">{{ consulta.especialidade }}</p>

                <div class="details d-flex align-items-center gap-3 mb-3">
                  <span class="d-flex align-items-center gap-1">
                    <i class="bi bi-calendar3"></i> {{ consulta.data }}
                  </span>
                  <span class="d-flex align-items-center gap-1">
                    <i class="bi bi-clock"></i> {{ consulta.hora }}
                  </span>
                  <span class="fw-bold text-dark">R$ {{ consulta.valor }}</span>
                </div>

                <!-- AÇÕES DINÂMICAS POR STATUS -->
                
                <!-- Caso: Agendada -->
                <button v-if="consulta.status === 'Agendada'" class="btn btn-enter d-flex align-items-center gap-2">
                  <i class="bi bi-camera-video-fill"></i> Entrar na Consulta
                </button>

                <!-- Caso: Concluída (Avaliação + Prescrição + Atestado) -->
                <div v-else-if="consulta.status === 'Concluída'" class="concluded-actions">
                  <div class="rating mb-3 d-flex align-items-center gap-2">
                    <div class="stars text-warning">
                      <i class="bi bi-star-fill" v-for="i in 5" :key="i"></i>
                    </div>
                    <small class="text-muted">Sua avaliação</small>
                  </div>
                  <div class="d-flex gap-2">
                    <button class="btn btn-outline-secondary btn-sm d-flex align-items-center gap-2 px-3 py-2">
                      <i class="bi bi-file-earmark-text"></i> Ver Prescrição
                    </button>
                    <button class="btn btn-link btn-sm text-dark text-decoration-none d-flex align-items-center gap-2">
                      <i class="bi bi-download"></i> Baixar Atestado
                    </button>
                  </div>
                </div>
              </div>
            </div>

            <!-- Badge Lateral Dinâmica -->
            <span class="status-badge" :class="consulta.status.toLowerCase()">
              {{ consulta.status }}
            </span>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, computed } from "vue";
import SidebarPatientComp from "../../components/patient/SidebarPatientComp.vue";

const activeTab = ref("Todas");

const consultas = ref([
  { id: 1, nome: "Dr. Carlos Mendes", especialidade: "Cardiologista", data: "15 Mar 2026", hora: "14:00", valor: "250.00", status: "Agendada" },
  { id: 2, nome: "Dr. Ricardo Santos", especialidade: "Psiquiatra", data: "15 Fev 2026", hora: "11:00", valor: "300.00", status: "Concluída" },
  { id: 3, nome: "Dra. Mariana Costa", especialidade: "Pediatra", data: "10 Jan 2026", hora: "08:30", valor: "180.00", status: "Cancelada" },
]);

const tabs = computed(() => [
  { label: "Todas", count: 6 },
  { label: "Agendadas", count: 2 },
  { label: "Concluídas", count: 3 },
  { label: "Canceladas", count: 1 },
]);

const filteredConsultas = computed(() => {
  if (activeTab.value === "Todas") return consultas.value;
  return consultas.value.filter(c => c.status === activeTab.value.slice(0, -1));
});

const getInitials = (nome) => {
  return nome.split(" ").filter(n => n.length > 3).slice(0, 2).map(n => n[0]).join("");
};
</script>

<style scoped>
.dashboard-wrapper { background-color: #f4f9f9; min-height: 100vh; }

/* Tabs */
.tabs-container { display: flex; background-color: #e9eff2; padding: 5px; border-radius: 12px; }
.tab-item { flex: 1; border: none; background: transparent; padding: 10px; font-weight: 500; color: #475569; border-radius: 10px; }
.tab-item.active { background-color: white; color: #000; box-shadow: 0 2px 8px rgba(0,0,0,0.05); }

/* Cards */
.consult-card { background: white; border-radius: 20px; border: 1px solid #e2e8f0; transition: opacity 0.3s; }
.card-cancelled { opacity: 0.7; }

.avatar-circle {
  width: 60px; height: 60px; border-radius: 50%;
  background-color: #DFF2F0; color: #03A1E0;
  display: flex; align-items: center; justify-content: center; font-weight: bold;
}

.specialty-text { color: #03A1E0; font-weight: 500; }
.details { color: #64748b; font-size: 0.9rem; }

/* Botões */
.btn-enter { background-color: #0468BF; color: white; border: none; border-radius: 10px; padding: 10px 20px; font-weight: 600; }

.btn-outline-secondary {
  border: 1px solid #e2e8f0;
  background: white;
  color: #334155;
  font-weight: 500;
  border-radius: 10px;
}

/* Badges */
.status-badge { padding: 6px 16px; border-radius: 20px; font-size: 0.75rem; font-weight: bold; }
.status-badge.agendada { background-color: #0468BF; color: white; }
.status-badge.concluída { background-color: #A3E4D7; color: #117A65; } /* Verde suave da imagem */
.status-badge.cancelada { background-color: transparent; border: 1px solid #CBD5E0; color: #64748B; }
</style>