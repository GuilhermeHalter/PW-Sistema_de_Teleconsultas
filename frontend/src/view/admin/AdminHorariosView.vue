<template>
  <div class="d-flex dashboard-wrapper">
    <SidebarAdminComp />
    <main class="content flex-grow-1 p-4">
      <header class="d-flex justify-content-between align-items-center mb-4">
        <div>
          <h3 class="fw-bold text-dark mb-1">Gerenciar Horários</h3>
          <p class="text-muted">Crie e gerencie horários para os médicos</p>
        </div>
        <button class="btn btn-danger px-4 py-2 rounded-3 fw-bold d-flex align-items-center gap-2" @click="abrirModal()">
          <i class="bi bi-plus-lg"></i> Novo Horário
        </button>
      </header>

      <div class="section-card p-3 mb-4 d-flex gap-3 flex-wrap">
        <select v-model="medicoFiltro" class="form-select rounded-3" style="max-width:280px" @change="carregarHorarios">
          <option value="">Todos os médicos</option>
          <option v-for="m in medicos" :key="m.id" :value="m.id">{{ m.nomeCompleto }}</option>
        </select>
        <div class="flex-grow-1"></div>
        <div class="d-flex gap-2 align-items-center">
          <span class="badge bg-success-soft text-success px-3 py-2">Disponíveis: {{ horariosDisponiveis }}</span>
          <span class="badge bg-warning-soft text-warning px-3 py-2">Reservados: {{ horariosReservados }}</span>
        </div>
      </div>

      <div v-if="loading" class="text-center py-5">
        <div class="spinner-border text-danger"></div>
      </div>

      <div v-else class="section-card overflow-hidden">
        <table class="table table-hover mb-0">
          <thead class="table-light">
            <tr>
              <th class="px-4 py-3">Médico</th>
              <th>Início</th>
              <th>Fim</th>
              <th>Disponível</th>
              <th class="text-end px-4">Ações</th>
            </tr>
          </thead>
          <tbody>
            <tr v-if="horarios.length === 0">
              <td colspan="5" class="text-center py-4 text-muted">Nenhum horário encontrado</td>
            </tr>
            <tr v-for="h in horarios" :key="h.id">
              <td class="px-4 py-3 fw-semibold small text-dark">{{ getNomeMedico(h) }}</td>
              <td class="small">{{ formatDataHora(h.data_hora_inicio) }}</td>
              <td class="small text-muted">{{ formatDataHora(h.data_hora_fim) }}</td>
              <td>
                <span class="badge rounded-pill" :class="h.disponivel ? 'bg-success-soft text-success' : 'bg-warning-soft text-warning'">
                  {{ h.disponivel ? 'Disponível' : 'Reservado' }}
                </span>
              </td>
              <td class="text-end px-4">
                <button class="btn btn-sm btn-outline-danger rounded-3 px-3" @click="excluir(h)" :disabled="!h.disponivel" :title="!h.disponivel ? 'Horário reservado' : 'Excluir'">
                  <i class="bi bi-trash"></i>
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Modal novo horário -->
      <div v-if="modalAberto" class="modal-overlay d-flex align-items-center justify-content-center" @click.self="fecharModal">
        <div class="modal-card p-4">
          <div class="d-flex justify-content-between align-items-center mb-4">
            <h5 class="fw-bold mb-0">Novo Horário</h5>
            <button class="btn btn-sm btn-outline-secondary rounded-circle" @click="fecharModal"><i class="bi bi-x"></i></button>
          </div>
          <div v-if="erroModal" class="alert alert-danger py-2 small mb-3">{{ erroModal }}</div>
          <div class="row g-3">
            <div class="col-12">
              <label class="form-label">Médico *</label>
              <select v-model="form.medicoId" class="form-select rounded-3">
                <option value="">Selecione um médico</option>
                <option v-for="m in medicos" :key="m.id" :value="m.id">{{ m.nomeCompleto }}</option>
              </select>
            </div>
            <div class="col-md-6">
              <label class="form-label">Data/Hora de Início *</label>
              <input v-model="form.inicio" type="datetime-local" class="form-control rounded-3" />
            </div>
            <div class="col-md-6">
              <label class="form-label">Data/Hora de Fim *</label>
              <input v-model="form.fim" type="datetime-local" class="form-control rounded-3" />
            </div>
          </div>
          <div class="d-flex gap-2 mt-4">
            <button class="btn btn-danger flex-grow-1 rounded-3 fw-bold" @click="salvar" :disabled="salvando">
              <span v-if="salvando" class="spinner-border spinner-border-sm me-2"></span>
              {{ salvando ? 'Criando...' : 'Criar Horário' }}
            </button>
            <button class="btn btn-outline-secondary rounded-3 px-4" @click="fecharModal">Cancelar</button>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, computed, reactive, onMounted } from 'vue'
import SidebarAdminComp from '../../components/admin/SidebarAdminComp.vue'
import { horarioService, medicoService } from '../../services/api.js'

const loading = ref(true)
const salvando = ref(false)
const horarios = ref([])
const medicos = ref([])
const medicoFiltro = ref('')
const modalAberto = ref(false)
const erroModal = ref('')
const form = reactive({ medicoId: '', inicio: '', fim: '' })

const horariosDisponiveis = computed(() => horarios.value.filter(h => h.disponivel).length)
const horariosReservados = computed(() => horarios.value.filter(h => !h.disponivel).length)

const formatDataHora = (iso) => iso ? new Date(iso).toLocaleString('pt-BR', { day:'2-digit', month:'2-digit', year:'numeric', hour:'2-digit', minute:'2-digit' }) : '—'

const getNomeMedico = (h) => {
  if (h.medicos && h.medicos.length > 0) {
    const id = h.medicos[0]
    const m = medicos.value.find(med => med.id === id)
    return m?.nomeCompleto || `Médico #${id}`
  }
  return '—'
}

const carregarHorarios = async () => {
  loading.value = true
  try {
    const params = medicoFiltro.value ? { medico_id: medicoFiltro.value } : {}
    const res = await horarioService.listar(params)
    horarios.value = res.data
  } catch (e) { console.error(e) }
  finally { loading.value = false }
}

const abrirModal = () => {
  erroModal.value = ''
  Object.assign(form, { medicoId: '', inicio: '', fim: '' })
  modalAberto.value = true
}

const fecharModal = () => { modalAberto.value = false }

const salvar = async () => {
  erroModal.value = ''
  if (!form.medicoId || !form.inicio || !form.fim) {
    erroModal.value = 'Preencha todos os campos obrigatórios.'
    return
  }
  if (new Date(form.fim) <= new Date(form.inicio)) {
    erroModal.value = 'O fim deve ser posterior ao início.'
    return
  }
  salvando.value = true
  try {
    await horarioService.criar({ data_hora_inicio: form.inicio, data_hora_fim: form.fim, disponivel: true, medico_id: form.medicoId })
    fecharModal()
    await carregarHorarios()
  } catch (e) {
    erroModal.value = 'Erro ao criar horário.'
  } finally { salvando.value = false }
}

const excluir = async (h) => {
  if (!confirm('Excluir este horário?')) return
  try { await horarioService.excluir(h.id); await carregarHorarios() }
  catch { alert('Erro ao excluir horário') }
}

onMounted(async () => {
  try {
    const res = await medicoService.listar()
    medicos.value = res.data
  } catch {}
  await carregarHorarios()
})
</script>

<style scoped>
@import url("https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css");
.dashboard-wrapper { background-color: #fff5f5; min-height: 100vh; }
.section-card { background: white; border-radius: 16px; border: 1px solid #e2e8f0; box-shadow: 0 2px 8px rgba(0,0,0,0.04); }
.form-label { font-size: 0.85rem; font-weight: 600; color: #1e293b; margin-bottom: 0.3rem; display: block; }
.form-control, .form-select { border: 1.5px solid #e2e8f0; padding: 10px 14px; }
.form-control:focus, .form-select:focus { border-color: #dc2626; box-shadow: 0 0 0 3px rgba(220,38,38,0.1); }
.bg-success-soft { background: #dcfce7; } .text-success { color: #16a34a !important; }
.bg-warning-soft { background: #fef9c3; } .text-warning { color: #ca8a04 !important; }
.modal-overlay { position: fixed; inset: 0; background: rgba(0,0,0,0.5); z-index: 1000; backdrop-filter: blur(2px); }
.modal-card { background: white; border-radius: 20px; width: 100%; max-width: 500px; box-shadow: 0 20px 60px rgba(0,0,0,0.2); }
</style>
