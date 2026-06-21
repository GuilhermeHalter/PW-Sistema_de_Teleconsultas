<template>
  <div class="d-flex dashboard-wrapper">
    <SidebarAdminComp />
    <main class="content flex-grow-1 p-4">
      <header class="mb-4">
        <h3 class="fw-bold text-dark mb-1">Gerenciar Pacientes</h3>
        <p class="text-muted">Visualize e gerencie os pacientes cadastrados</p>
      </header>

      <div class="section-card p-3 mb-4">
        <div class="position-relative">
          <i class="bi bi-search position-absolute" style="left:14px;top:50%;transform:translateY(-50%);color:#94a3b8"></i>
          <input v-model="busca" class="form-control rounded-3 ps-5" placeholder="Buscar por nome, e-mail ou CPF..." />
        </div>
      </div>

      <div v-if="loading" class="text-center py-5">
        <div class="spinner-border text-danger"></div>
      </div>

      <div v-else class="section-card overflow-hidden">
        <table class="table table-hover mb-0">
          <thead class="table-light">
            <tr>
              <th class="px-4 py-3">Paciente</th>
              <th>CPF</th>
              <th>E-mail</th>
              <th>Status</th>
              <th class="text-end px-4">Ações</th>
            </tr>
          </thead>
          <tbody>
            <tr v-if="pacientesFiltrados.length === 0">
              <td colspan="5" class="text-center py-4 text-muted">Nenhum paciente encontrado</td>
            </tr>
            <tr v-for="p in pacientesFiltrados" :key="p.id">
              <td class="px-4 py-3">
                <div class="d-flex align-items-center gap-3">
                  <div class="avatar-sm bg-blue-soft text-primary fw-bold rounded-circle d-flex align-items-center justify-content-center">{{ initials(p.nomeCompleto) }}</div>
                  <span class="fw-semibold text-dark">{{ p.nomeCompleto }}</span>
                </div>
              </td>
              <td class="font-monospace small text-muted">{{ p.cpf || '—' }}</td>
              <td class="small text-muted">{{ p.email }}</td>
              <td><span class="badge bg-success-soft text-success">Ativo</span></td>
              <td class="text-end px-4">
                <button class="btn btn-sm btn-outline-secondary rounded-3 me-1 px-3" @click="abrirModal(p)">
                  <i class="bi bi-pencil"></i>
                </button>
                <button class="btn btn-sm btn-outline-danger rounded-3 px-3" @click="excluir(p)">
                  <i class="bi bi-trash"></i>
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Modal editar -->
      <div v-if="modalAberto" class="modal-overlay d-flex align-items-center justify-content-center" @click.self="fecharModal">
        <div class="modal-card p-4">
          <div class="d-flex justify-content-between align-items-center mb-4">
            <h5 class="fw-bold mb-0">Editar Paciente</h5>
            <button class="btn btn-sm btn-outline-secondary rounded-circle" @click="fecharModal"><i class="bi bi-x"></i></button>
          </div>
          <div v-if="erroModal" class="alert alert-danger py-2 small mb-3">{{ erroModal }}</div>
          <div class="row g-3">
            <div class="col-12">
              <label class="form-label">Nome Completo</label>
              <input v-model="form.nomeCompleto" class="form-control rounded-3" />
            </div>
            <div class="col-12">
              <label class="form-label">E-mail</label>
              <input v-model="form.email" type="email" class="form-control rounded-3" />
            </div>
            <div class="col-12">
              <label class="form-label">CPF (não editável)</label>
              <input v-model="form.cpf" class="form-control rounded-3 bg-light" disabled />
            </div>
          </div>
          <div class="d-flex gap-2 mt-4">
            <button class="btn btn-danger flex-grow-1 rounded-3 fw-bold" @click="salvar" :disabled="salvando">
              <span v-if="salvando" class="spinner-border spinner-border-sm me-2"></span>
              {{ salvando ? 'Salvando...' : 'Salvar Alterações' }}
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
import { pacienteService } from '../../services/api.js'

const loading = ref(true)
const salvando = ref(false)
const pacientes = ref([])
const busca = ref('')
const modalAberto = ref(false)
const editando = ref(null)
const erroModal = ref('')
const form = reactive({ nomeCompleto: '', email: '', cpf: '' })

const pacientesFiltrados = computed(() => {
  if (!busca.value) return pacientes.value
  const b = busca.value.toLowerCase()
  return pacientes.value.filter(p =>
    p.nomeCompleto?.toLowerCase().includes(b) ||
    p.email?.toLowerCase().includes(b) ||
    p.cpf?.includes(b)
  )
})

const initials = (nome) => nome ? nome.split(' ').filter(n=>n.length>0).slice(0,2).map(n=>n[0]).join('') : '?'

const carregarPacientes = async () => {
  loading.value = true
  try { const res = await pacienteService.listar(); pacientes.value = res.data }
  catch (e) { console.error(e) }
  finally { loading.value = false }
}

const abrirModal = (p) => {
  erroModal.value = ''
  editando.value = p
  Object.assign(form, { nomeCompleto: p.nomeCompleto, email: p.email, cpf: p.cpf })
  modalAberto.value = true
}

const fecharModal = () => { modalAberto.value = false; editando.value = null }

const salvar = async () => {
  erroModal.value = ''
  salvando.value = true
  try {
    await pacienteService.atualizar(editando.value.id, { nomeCompleto: form.nomeCompleto, email: form.email })
    fecharModal()
    await carregarPacientes()
  } catch (e) {
    erroModal.value = 'Erro ao salvar alterações.'
  } finally { salvando.value = false }
}

const excluir = async (p) => {
  if (!confirm(`Excluir o paciente "${p.nomeCompleto}"?`)) return
  try { await pacienteService.excluir(p.id); await carregarPacientes() }
  catch { alert('Erro ao excluir paciente.') }
}

onMounted(carregarPacientes)
</script>

<style scoped>
@import url("https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css");
.dashboard-wrapper { background-color: #fff5f5; min-height: 100vh; }
.section-card { background: white; border-radius: 16px; border: 1px solid #e2e8f0; box-shadow: 0 2px 8px rgba(0,0,0,0.04); }
.avatar-sm { width: 38px; height: 38px; min-width: 38px; font-size: 0.85rem; }
.bg-blue-soft { background: #dbeafe; }
.bg-success-soft { background: #dcfce7; } .text-success { color: #16a34a !important; }
.form-label { font-size: 0.85rem; font-weight: 600; color: #1e293b; margin-bottom: 0.3rem; display: block; }
.form-control { border: 1.5px solid #e2e8f0; padding: 10px 14px; }
.form-control:focus { border-color: #dc2626; box-shadow: 0 0 0 3px rgba(220,38,38,0.1); }
.modal-overlay { position: fixed; inset: 0; background: rgba(0,0,0,0.5); z-index: 1000; backdrop-filter: blur(2px); }
.modal-card { background: white; border-radius: 20px; width: 100%; max-width: 500px; box-shadow: 0 20px 60px rgba(0,0,0,0.2); }
</style>
