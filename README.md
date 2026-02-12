# Sistema de Teleconsultas

## Situação Problema
Com o avanço da tecnologia e a crescente demanda por atendimentos médicos remotos, especialmente após a popularização da telemedicina, tornou-se evidente a necessidade de sistemas seguros, organizados e confiáveis para a realização de teleconsultas.

Atualmente, muitos profissionais da saúde enfrentam dificuldades na gestão de agendas, confirmação de pagamentos, organização de horários e controle de acesso às consultas online. Em diversos casos, o envio manual de links de videoconferência, a ausência de validação automática de pagamento e falhas na autenticação de usuários geram atrasos, cancelamentos, conflitos de horários e riscos à segurança das informações.

Além disso, pacientes frequentemente encontram problemas como falta de confirmação clara da consulta, insegurança no processo de pagamento e dificuldade de acesso ao link da chamada no momento do atendimento.

## Resumo da Solução

Sistema de Teleconsulta que permite o gerenciamento de médicos e seus horários de atendimento, oferecendo um fluxo completo de check-in do paciente com validação de pagamento. Após a confirmação, o sistema libera o link da chamada, garantindo controle de agenda, segurança no acesso e uma experiência organizada de atendimento médico online.

## Funcionalidades

- Cadastro e gerenciamento de médicos
- Definição de horários de atendimento
- Check-in do paciente com validação de pagamento
- Liberação automática do link da consulta após confirmação
- Controle de agenda e segurança nos atendimentos


## Tecnologias

- **Front-end**: Vue.js
- **Back-end**: Django (Python)
- **Banco de Dados**: MySQL
- **Autenticação:** JWT
- **Pagamento:** Stripe / PayPal
- **Videochamada:** WebRTC / Twilio Video
- **Testes**: Cypress (Testes)
