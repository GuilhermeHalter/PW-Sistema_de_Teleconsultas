<template>
  <div class="d-flex dashboard-wrapper">
    <SidebarAdminComp />
    <main class="content flex-grow-1 p-4">
      <header class="mb-4">
        <h3 class="fw-bold text-dark mb-1">Painel Administrativo</h3>
        <p class="text-muted">Visão geral do sistema MedConnect</p>
      </header>

      <div v-if="loading" class="text-center py-5">
        <div class="spinner-border text-danger" role="status"></div>
      </div>

      <div v-else>
        <div class="row g-4 mb-5">
          <div class="col-md-3">
            <div class="stat-card red-theme d-flex align-items-center gap-3">
              <div class="icon-box"><i class="bi bi-heart-pulse"></i></div>
              <div>
                <h4 class="mb-0 fw-bold">{{ stats.medicos }}</h4>
                <p class="mb-0 text-muted small">Médicos</p>
              </div>
            </div>
          </div>
          <div class="col-md-3">
            <div class="stat-card blue-theme d-flex align-items-center gap-3">
              <div class="icon-box"><i class="bi bi-people"></i></div>
              <div>
                <h4 class="mb-0 fw-bold">{{ stats.pacientes }}</h4>
                <p class="mb-0 text-muted small">Pacientes</p>
              </div>
            </div>
          </div>
          <div class="col-md-3">
            <div class="stat-card green-theme d-flex align-items-center gap-3">
              <div class="icon-box"><i class="bi bi-calendar-check"></i></div>
              <div>
                <h4 class="mb-0 fw-bold">{{ stats.consultas }}</h4>
                <p class="mb-0 text-muted small">Consultas</p>
              </div>
            </div>
          </div>
          <div class="col-md-3">
            <div class="stat-card yellow-theme d-flex align-items-center gap-3">
              <div class="icon-box"><i class="bi bi-clock"></i></div>
              <div>
                <h4 class="mb-0 fw-bold">{{ stats.horarios }}</h4>
                <p class="mb-0 text-muted small">Horários Cadastrados</p>
              </div>
            </div>
          </div>
        </div>

        <div class="row g-4">
          <div class="col-lg-8">
            <div class="section-card p-4">
              <div class="d-flex justify-content-between align-items-center mb-4">
                <h5 class="fw-bold mb-0"><i class="bi bi-calendar-check me-2 text-danger"></i>Consultas Recentes</h5>
                <router-link to="/admin/consultas" class="btn btn-sm btn-outline-danger rounded-3">Ver todas</router-link>
              </div>
              <div v-if="consultasRecentes.length === 0" class="text-center py-4 text-muted">Nenhuma consulta</div>
              <div v-else class="d-flex flex-column gap-2">
                <div v-for="c in consultasRecentes" :key="c.id" class="consult-row d-flex align-items-center justify-content-between p-3 rounded-3">
                  <div>
                    <p class="mb-0 fw-semibold small text-dark">{{ c.paciente_nome }} → {{ c.medico_nome }}</p>
                    <small class="text-muted">{{ formatData(c.horario_inicio) }}</small>
                  </div>
                  <span class="badge rounded-pill" :class="statusBadge(c.status)">{{ statusLabel(c.status) }}</span>
                </div>
              </div>
            </div>
          </div>
          <div class="col-lg-4">
            <div class="section-card p-4">
              <h5 class="fw-bold mb-4"><i class="bi bi-lightning-fill me-2 text-danger"></i>Ações Rápidas</h5>
              <div class="d-flex flex-column gap-2">
                <router-link to="/admin/medicos" class="btn btn-action-card d-flex align-items-center gap-3 p-3 text-decoration-none">
                  <div class="action-icon bg-red-soft"><i class="bi bi-heart-pulse text-danger"></i></div>
                  <div>
                    <p class="mb-0 fw-semibold small text-dark">Gerenciar Médicos</p>
                    <small class="text-muted">Cadastrar, editar, remover</small>
                  </div>
                </router-link>
                <router-link to="/admin/pacientes" class="btn btn-action-card d-flex align-items-center gap-3 p-3 text-decoration-none">
                  <div class="action-icon bg-blue-soft"><i class="bi bi-people text-primary"></i></div>
                  <div>
                    <p class="mb-0 fw-semibold small text-dark">Gerenciar Pacientes</p>
                    <small class="text-muted">Visualizar e editar</small>
                  </div>
                </router-link>
                <router-link to="/admin/consultas" class="btn btn-action-card d-flex align-items-center gap-3 p-3 text-decoration-none">
                  <div class="action-icon bg-green-soft"><i class="bi bi-calendar-check text-success"></i></div>
                  <div>
                    <p class="mb-0 fw-semibold small text-dark">Gerenciar Consultas</p>
                    <small class="text-muted">Status, cancelar, finalizar</small>
                  </div>
                </router-link>
                <router-link to="/admin/horarios" class="btn btn-action-card d-flex align-items-center gap-3 p-3 text-decoration-none">
                  <div class="action-icon bg-yellow-soft"><i class="bi bi-clock text-warning"></i></div>
                  <div>
                    <p class="mb-0 fw-semibold small text-dark">Gerenciar Horários</p>
                    <small class="text-muted">Criar e excluir slots</small>
                  </div>
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
import { ref, onMounted } from 'vue'
import SidebarAdminComp from '../../components/admin/SidebarAdminComp.vue'
import { medicoService, pacienteService, consultaService, horarioService } from '../../services/api.js'

const loading = ref(true)
const stats = ref({ medicos: 0, pacientes: 0, consultas: 0, horarios: 0 })
const consultasRecentes = ref([])

const formatData = (iso) => iso ? new Date(iso).toLocaleDateString('pt-BR', { day:'2-digit', month:'short', year:'numeric' }) : '-'

const statusLabel = (s) => ({ CONFIRMADA:'Confirmada', AGUARDANDO_PAGAMENTO:'Pend. Pgto', CANCELADA:'Cancelada', FINALIZADA:'Finalizada' })[s] || s
const statusBadge = (s) => {
  if (s === 'CONFIRMADA') return 'bg-success-soft text-success'
  if (s === 'AGUARDANDO_PAGAMENTO') return 'bg-warning-soft text-warning'
  if (s === 'CANCELADA') return 'bg-light text-muted'
  return 'bg-blue-soft text-primary'
}

onMounted(async () => {
  try {
    const [med, pac, con, hor] = await Promise.all([
      medicoService.listar(),
      pacienteService.listar(),
      consultaService.listar(),
      horarioService.listar()
    ])
    stats.value = { medicos: med.data.length, pacientes: pac.data.length, consultas: con.data.length, horarios: hor.data.length }
    consultasRecentes.value = con.data.slice(0, 6)
  } catch (e) { console.error(e) }
  finally { loading.value = false }
})
</script>

<style scoped>
@import url("https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css");
.dashboard-wrapper { background-color: #fff5f5; min-height: 100vh; font-family: 'Inter', sans-serif; }
.stat-card { padding: 20px; border-radius: 16px; border: 1px solid #e2e8f0; background: white; }
.stat-card .icon-box { width: 48px; height: 48px; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 1.4rem; color: white; }
.red-theme { background-color: #fff5f5; border-color: #fecaca; } .red-theme .icon-box { background: #dc2626; }
.blue-theme { background-color: #eff6ff; border-color: #bfdbfe; } .blue-theme .icon-box { background: #2563eb; }
.green-theme { background-color: #f0fdf4; border-color: #bbf7d0; } .green-theme .icon-box { background: #16a34a; }
.yellow-theme { background-color: #fefce8; border-color: #fef08a; } .yellow-theme .icon-box { background: #ca8a04; }
.section-card { background: white; border-radius: 16px; border: 1px solid #e2e8f0; box-shadow: 0 2px 8px rgba(0,0,0,0.04); }
.consult-row { background: #fafafa; border: 1px solid #f1f5f9; }
.btn-action-card { background: white; border: 1px solid #f1f5f9; border-radius: 12px; text-align: left; }
.btn-action-card:hover { border-color: #fecaca; background: #fff5f5; }
.action-icon { width: 40px; height: 40px; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 1.1rem; flex-shrink: 0; }
.bg-red-soft { background: #fee2e2; } .bg-blue-soft { background: #dbeafe; } .bg-green-soft { background: #dcfce7; } .bg-yellow-soft { background: #fef9c3; }
.bg-success-soft { background: #dcfce7; } .text-success { color: #16a34a !important; }
.bg-warning-soft { background: #fef9c3; } .text-warning { color: #ca8a04 !important; }
</style>
