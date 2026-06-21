<template>
  <div class="d-flex dashboard-wrapper">
    <SidebarPatientComp />

    <main class="content flex-grow-1 p-4">
      <div class="mb-4">
        <button class="btn btn-back d-flex align-items-center gap-2 fw-medium" @click="$router.back()">
          <i class="bi bi-arrow-left"></i> Voltar
        </button>
      </div>

      <div class="payment-container mx-auto">
        <h3 class="fw-bold text-dark mb-1 text-center">Pagamento da Consulta</h3>
        <p class="text-muted text-center mb-5">Confirme o pagamento para garantir sua consulta</p>

        <!-- Resumo da consulta -->
        <div v-if="consulta" class="section-card p-4 mb-4">
          <h6 class="fw-bold mb-3 text-dark"><i class="bi bi-calendar-check me-2 text-azure"></i>Resumo</h6>
          <div class="row g-2 text-sm">
            <div class="col-6 text-muted">Médico</div>
            <div class="col-6 fw-semibold text-dark">{{ consulta.medico_nome }}</div>
            <div class="col-6 text-muted">Data</div>
            <div class="col-6 fw-semibold text-dark">{{ formatDataHora(consulta.horario_inicio) }}</div>
            <div class="col-6 text-muted">Status</div>
            <div class="col-6">
              <span class="badge bg-warning-soft text-warning fw-semibold">Aguardando Pagamento</span>
            </div>
          </div>
          <hr class="my-3" />
          <div class="d-flex justify-content-between align-items-center">
            <span class="fw-bold text-dark">Total</span>
            <span class="fw-bold fs-5 text-blue-deep">R$ 250,00</span>
          </div>
        </div>

        <!-- Simulação de pagamento -->
        <div class="section-card p-4 mb-4">
          <h6 class="fw-bold mb-4 text-dark"><i class="bi bi-credit-card me-2 text-azure"></i>Dados do Cartão</h6>

          <div class="row g-3">
            <div class="col-12">
              <label class="form-label text-muted small fw-semibold">Número do Cartão</label>
              <input
                type="text"
                class="form-control rounded-3"
                placeholder="1234 5678 9012 3456"
                v-model="cartao.numero"
                maxlength="19"
                @input="formatarCartao"
              />
            </div>
            <div class="col-12">
              <label class="form-label text-muted small fw-semibold">Nome no Cartão</label>
              <input type="text" class="form-control rounded-3" placeholder="Nome completo" v-model="cartao.nome" />
            </div>
            <div class="col-6">
              <label class="form-label text-muted small fw-semibold">Validade</label>
              <input type="text" class="form-control rounded-3" placeholder="MM/AA" v-model="cartao.validade" maxlength="5" />
            </div>
            <div class="col-6">
              <label class="form-label text-muted small fw-semibold">CVV</label>
              <input type="text" class="form-control rounded-3" placeholder="123" v-model="cartao.cvv" maxlength="3" />
            </div>
          </div>

          <div class="payment-info mt-3 p-3 rounded-3">
            <small class="text-muted"><i class="bi bi-info-circle me-1 text-azure"></i>Ambiente de demonstração. Use qualquer dado para simular o pagamento.</small>
          </div>
        </div>

        <div v-if="erro" class="alert alert-danger py-2 small mb-3">{{ erro }}</div>

        <div v-if="pago" class="alert alert-success p-4 text-center mb-4">
          <i class="bi bi-check-circle-fill fs-1 text-success d-block mb-2"></i>
          <h5 class="fw-bold">Pagamento Confirmado!</h5>
          <p class="mb-0 small">Sua consulta foi confirmada. O link de acesso foi gerado.</p>
        </div>

        <button
          v-if="!pago"
          class="btn btn-primary-custom w-100 py-3 fw-bold rounded-3 shadow-sm"
          :disabled="pagando || !formValido"
          @click="processarPagamento"
        >
          <span v-if="pagando" class="spinner-border spinner-border-sm me-2"></span>
          <i v-else class="bi bi-lock-fill me-2"></i>
          {{ pagando ? 'Processando...' : 'Confirmar Pagamento' }}
        </button>

        <button
          v-if="pago"
          class="btn btn-success w-100 py-3 fw-bold rounded-3 shadow-sm"
          @click="irParaSala"
        >
          <i class="bi bi-camera-video-fill me-2"></i> Acessar Consulta
        </button>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import SidebarPatientComp from '../../components/patient/SidebarPatientComp.vue'
import { consultaService } from '../../services/api.js'

const route = useRoute()
const router = useRouter()

const consulta = ref(null)
const pagando = ref(false)
const pago = ref(false)
const erro = ref('')
const linkConsulta = ref('')

const cartao = ref({ numero: '', nome: '', validade: '', cvv: '' })

const consultaId = route.query.consultaId

const formValido = computed(() =>
  cartao.value.numero.length >= 16 &&
  cartao.value.nome.length >= 3 &&
  cartao.value.validade.length === 5 &&
  cartao.value.cvv.length === 3
)

const formatarCartao = () => {
  let v = cartao.value.numero.replace(/\D/g, '').slice(0, 16)
  cartao.value.numero = v.replace(/(.{4})/g, '$1 ').trim()
}

const formatDataHora = (iso) => {
  if (!iso) return '-'
  return new Date(iso).toLocaleString('pt-BR', { day: '2-digit', month: 'short', year: 'numeric', hour: '2-digit', minute: '2-digit' })
}

const processarPagamento = async () => {
  erro.value = ''
  pagando.value = true
  try {
    await new Promise(resolve => setTimeout(resolve, 1500))
    const res = await consultaService.confirmarPagamento(consultaId)
    consulta.value = res.data
    linkConsulta.value = res.data.link_video
    pago.value = true
  } catch (e) {
    erro.value = e.response?.data?.error || 'Erro ao processar pagamento. Tente novamente.'
  } finally {
    pagando.value = false
  }
}

const irParaSala = () => {
  router.push({ name: 'sala-teleconsulta', query: { consultaId, link: linkConsulta.value } })
}

onMounted(async () => {
  if (!consultaId) {
    router.push({ name: 'agendamento' })
    return
  }
  try {
    const res = await consultaService.buscarPorId(consultaId)
    consulta.value = res.data
  } catch (e) {
    console.error(e)
  }
})
</script>

<style scoped>
@import url("https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css");

.dashboard-wrapper { background-color: #f4f9f9; min-height: 100vh; }
.payment-container { max-width: 560px; }

.section-card { background: white; border-radius: 20px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.02); }

.form-control { border: 1px solid #cbd5e1; padding: 10px 14px; border-radius: 10px; }
.form-control:focus { border-color: #0468BF; box-shadow: 0 0 0 3px rgba(4,104,191,0.1); }

.btn-primary-custom { background-color: #0468BF; border: none; color: white; transition: background-color 0.2s; }
.btn-primary-custom:hover:not(:disabled) { background-color: #0060B4; }
.btn-primary-custom:disabled { background-color: #94a3b8; }

.btn-back { border: none; background: none; padding: 0; font-size: 0.9rem; color: #03A1E0; }
.btn-back:hover { color: #0060B4; }

.text-blue-deep { color: #0468BF; }
.text-azure { color: #03A1E0; }

.bg-warning-soft { background-color: #fef5ea; } .text-warning { color: #f57c00 !important; }
.payment-info { background-color: #f0faff; border: 1px solid #bae6fd; }
</style>
