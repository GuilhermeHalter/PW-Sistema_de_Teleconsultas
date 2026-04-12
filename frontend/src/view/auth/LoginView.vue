<template>
  <div class="login-wrapper d-flex justify-content-center align-items-center vh-100">
    <div class="login-card p-4 p-md-5">
      <h2 class="title fw-bold mb-2">Bem-vindo de volta!</h2>
      <p class="subtitle mb-4">Entre com suas credenciais para acessar sua conta</p>

      <div class="toggle-container d-flex mb-4">
        <router-link 
          to="/login" 
          class="toggle-btn flex-fill text-center text-decoration-none"
          :class="{ active: route.path === '/login' }"
        >
          Entrar
        </router-link>

        <router-link 
          to="/cadastro" 
          class="toggle-btn flex-fill text-center text-decoration-none"
          :class="{ active: route.path === '/cadastro' }"
        >
          Cadastrar
        </router-link>
      </div>

      <form @submit.prevent>
        <div class="mb-3">
          <label class="form-label">E-mail</label>
          <div class="input-wrapper position-relative">
            <i class="bi bi-envelope position-absolute icon-left"></i>
            <input 
              v-model="email"
              type="email" 
              class="form-control custom-input" 
              placeholder="seu@email.com" 
            />
          </div>
        </div>

        <div class="mb-3">
          <label class="form-label">Senha</label>
          <div class="input-wrapper position-relative">
            <i class="bi bi-lock position-absolute icon-left"></i>
            <input 
              v-model="password"
              :type="showPassword ? 'text' : 'password'" 
              class="form-control custom-input pe-5" 
              placeholder="........" 
            />
            <i 
              class="bi position-absolute icon-right cursor-pointer" 
              :class="showPassword ? 'bi-eye' : 'bi-eye-slash'" 
              @click="showPassword = !showPassword">
            </i>
          </div>
        </div>

        <div class="d-flex justify-content-between align-items-center mb-4 mt-2">
          <div class="form-check d-flex align-items-center">
            <input class="form-check-input custom-checkbox mt-0 me-2" type="checkbox" id="lembrar" />
            <label class="form-check-label text-muted" for="lembrar" style="font-size: 0.9rem;">
              Lembrar de mim
            </label>
          </div>

          <a href="#" class="brand-link text-decoration-none" style="font-size: 0.9rem;">
            Esqueceu a senha?
          </a>
        </div>

        <button class="btn btn-primary-custom w-100 py-2 mb-4">
          Entrar
        </button>
      </form>

      <div class="divider d-flex align-items-center mb-4">
        <hr class="flex-grow-1" />
        <span class="mx-3 text-muted text-uppercase" style="font-size: 0.75rem;">
          OU CONTINUE COM
        </span>
        <hr class="flex-grow-1" />
      </div>

      <div class="row g-3 mb-4">
        <div class="col-6">
          <button class="btn btn-social w-100 d-flex align-items-center justify-content-center gap-2">
            <i class="bi bi-google text-dark"></i>
            <span class="text-dark">Google</span>
          </button>
        </div>

        <div class="col-6">
          <button class="btn btn-social w-100 d-flex align-items-center justify-content-center gap-2">
            <i class="bi bi-github text-dark"></i>
            <span class="text-dark">GitHub</span>
          </button>
        </div>
      </div>

      <p class="text-center mt-3 mb-0 text-muted" style="font-size: 0.9rem;">
        Não tem uma conta?
        <router-link to="/cadastro" class="brand-link text-decoration-none">
          Cadastre-se
        </router-link>
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()

const showPassword = ref(false)
const email = ref('')
const password = ref('')
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Merriweather:wght@700&family=Lora:ital@0;1&family=Inter:wght@400;500&display=swap');
@import url("https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css");

:root {
  --primary-color: #00A09D;
  --bg-toggle: #E6F3F3;
}

body {
  background-color: #FAFAFC;
  font-family: 'Inter', sans-serif;
}

.login-wrapper {
  background-color: #FAFAFC;
}

.login-card {
  width: 100%;
  max-width: 480px;
  background: transparent;
}

.title {
  font-family: 'Merriweather', serif;
  color: #1A202C;
  font-size: 1.8rem;
}

.subtitle {
  color: #4A5568;
  font-family: 'Lora', serif;
  font-size: 0.95rem;
}

.toggle-container {
  background-color: var(--bg-toggle);
  border-radius: 8px;
  padding: 4px;
}

.toggle-btn {
  border: none;
  background: transparent;
  padding: 10px 0;
  border-radius: 6px;
  color: #4A5568;
  font-family: 'Lora', serif;
  transition: 0.3s;
}

.toggle-btn.active {
  background-color: #fff;
  color: #1A202C;
  box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}

.custom-input {
  padding-left: 2.6rem;
  border-radius: 8px;
}

.input-wrapper .icon-left {
  left: 14px;
  top: 50%;
  transform: translateY(-50%);
  position: absolute;
}

.input-wrapper .icon-right {
  right: 14px;
  top: 50%;
  transform: translateY(-50%);
  position: absolute;
}

.btn-primary-custom {
  background-color: var(--primary-color);
  border: none;
  border-radius: 8px;
  color: white;
}

.btn-social {
  background: white;
  border: 1px solid #E2E8F0;
  border-radius: 8px;
}

.brand-link {
  color: var(--primary-color);
}

.cursor-pointer {
  cursor: pointer;
}
</style>