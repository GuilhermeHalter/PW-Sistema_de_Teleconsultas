<template>
  <div class="d-flex dashboard-wrapper">
    <SidebarAdminComp />
    <main class="content flex-grow-1 p-4">
      <header class="mb-4">
        <h3 class="fw-bold text-dark mb-1">Gerenciar Consultas</h3>
        <p class="text-muted">Visualize e gerencie todas as consultas do sistema</p>
      </header>

      <div class="section-card p-3 mb-4 d-flex gap-3 flex-wrap">
        <div class="flex-grow-1 position-relative">
          <i class="bi bi-search position-absolute" style="left:14px;top:50%;transform:translateY(-50%);color:#94a3b8"></i>
          <input v-model="busca" class="form-control rounded-3 ps-5" placeholder="Buscar por médico ou paciente..." />
        </div>
        <select v-model="filtroStatus" class="form-select rounded-3" style="width:200px">
          <option value="">Todos os status</option>
          <option value="AGUARDANDO_PAGAMENTO">Aguardando Pgto</option>
          <option value="CONFIRMADA">Confirmada</option>
          <option value="FINALIZADA">Finalizada</option>
          <option value="CANCELADA">Cancelada</option>
        </select>
      </div>

      <div v-if="loading" class="text-center py-5">
        <div class="spinner-border text-danger"></div>
      </div>

      <div v-else class="section-card overflow-hidden">
        <table class="table table-hover mb-0">
          <thead class="table-light">
            <tr>
              <th class="px-4 py-3">Paciente</th>
              <th>Médico</th>
              <th>Data/Hora</th>
              <th>Status</th>
              <th class="text-end px-4">Ações</th>
            </tr>
          </thead>
          <tbody>
            <tr v-if="consultasFiltradas.length === 0">
              <td colspan="5" class="text-center py-4 text-muted">Nenhuma consulta encontrada</td>
            </tr>
            <tr v-for="c in consultasFiltradas" :key="c.id">
              <td class="px-4 py-3 fw-semibold small text-dark">{{ c.paciente_nome }}</td>
              <td class="small text-muted">{{ c.medico_nome }}</td>
              <td class="small text-muted">{{ formatDataHora(c.horario_inicio) }}</td>
              <td><span class="badge rounded-pill" :class="statusBadge(c.status)">{{ statusLabel(c.status) }}</span></td>
              <td class="text-end px-4">
                <div class="d-flex gap-1 justify-content-end">
                  <button v-if="c.status === 'AGUARDANDO_PAGAMENTO'" class="btn btn-sm btn-success rounded-3 px-2" title="Confirmar pagamento" @click="confirmarPagamento(c)">
                    <i class="bi bi-credit-card"></i>
                  </button>
                  <button v-if="c.status === 'CONFIRMADA'" class="btn btn-sm btn-primary rounded-3 px-2" title="Finalizar" @click="finalizar(c)">
                    <i class="bi bi-check-lg"></i>
                  </button>
                  <button v-if="['AGUARDANDO_PAGAMENTO','CONFIRMADA'].includes(c.status)" class="btn btn-sm btn-warning rounded-3 px-2" title="Cancelar" @click="cancelar(c)">
                    <i class="bi bi-x-lg"></i>
                  </button>
                  <button class="btn btn-sm btn-outline-danger rounded-3 px-2" title="Excluir" @click="excluir(c)">
                    <i class="bi bi-trash"></i>
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import SidebarAdminComp from '../../components/admin/SidebarAdminComp.vue'
import { consultaService } from '../../services/api.js'

const loading = ref(true)
const consultas = ref([])
const busca = ref('')
const filtroStatus = ref('')

const consultasFiltradas = computed(() => {
  let list = consultas.value
  if (filtroStatus.value) list = list.filter(c => c.status === filtroStatus.value)
  if (busca.value) {
    const b = busca.value.toLowerCase()
    list = list.filter(c => c.paciente_nome?.toLowerCase().includes(b) || c.medico_nome?.toLowerCase().includes(b))
  }
  return list
})

const formatDataHora = (iso) => iso ? new Date(iso).toLocaleString('pt-BR', { day:'2-digit', month:'short', hour:'2-digit', minute:'2-digit' }) : '—'

const statusLabel = (s) => ({ CONFIRMADA:'Confirmada', AGUARDANDO_PAGAMENTO:'Aguard. Pgto', CANCELADA:'Cancelada', FINALIZADA:'Finalizada' })[s] || s
const statusBadge = (s) => ({
  CONFIRMADA: 'bg-success-soft text-success',
  AGUARDANDO_PAGAMENTO: 'bg-warning-soft text-warning',
  CANCELADA: 'bg-light text-muted',
  FINALIZADA: 'bg-blue-soft text-primary'
})[s] || 'bg-light text-muted'

const carregarConsultas = async () => {
  loading.value = true
  try { const res = await consultaService.listar(); consultas.value = res.data }
  catch (e) { console.error(e) }
  finally { loading.value = false }
}

const confirmarPagamento = async (c) => {
  try { await consultaService.confirmarPagamento(c.id); await carregarConsultas() }
  catch (e) { alert(e.response?.data?.error || 'Erro ao confirmar pagamento') }
}

const finalizar = async (c) => {
  if (!confirm('Finalizar esta consulta?')) return
  try { await consultaService.finalizar(c.id); await carregarConsultas() }
  catch (e) { alert(e.response?.data?.error || 'Erro ao finalizar') }
}

const cancelar = async (c) => {
  if (!confirm('Cancelar esta consulta?')) return
  try { await consultaService.cancelar(c.id); await carregarConsultas() }
  catch (e) { alert(e.response?.data?.error || 'Erro ao cancelar') }
}

const excluir = async (c) => {
  if (!confirm('Excluir permanentemente esta consulta?')) return
  try { await consultaService.excluir(c.id); await carregarConsultas() }
  catch { alert('Erro ao excluir consulta') }
}

onMounted(carregarConsultas)
</script>

<style scoped>
@import url("https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css");
.dashboard-wrapper { background-color: #fff5f5; min-height: 100vh; }
.section-card { background: white; border-radius: 16px; border: 1px solid #e2e8f0; box-shadow: 0 2px 8px rgba(0,0,0,0.04); }
.form-control, .form-select { border: 1.5px solid #e2e8f0; padding: 10px 14px; }
.form-control:focus, .form-select:focus { border-color: #dc2626; box-shadow: 0 0 0 3px rgba(220,38,38,0.1); }
.bg-success-soft { background: #dcfce7; } .text-success { color: #16a34a !important; }
.bg-warning-soft { background: #fef9c3; } .text-warning { color: #ca8a04 !important; }
.bg-blue-soft { background: #dbeafe; }
</style>
