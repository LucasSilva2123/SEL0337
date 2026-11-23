# SEL0337 - Prática 5 (Checkpoint 1): Configuração do systemd em Linux Embarcado

**Disciplina:** SEL0337 - Projetos em Sistemas Embarcados (EESC-USP)  
**Integrantes:** Gabriel Suerdieck Nardelli e Lucas Manoel Freitas da Silva  

---

## 1. Visão Geral

Este repositório reúne os arquivos referentes ao **Checkpoint 1 da Prática 5**, cujo objetivo é configurar uma unidade de serviço personalizada (`systemd` *unit file*) no Raspberry Pi OS para gerenciar automaticamente uma aplicação em Python durante os eventos de inicialização (*boot*) e encerramento (*stop*/*reboot*/*shutdown*) do sistema operacional.

A aplicação implementa uma sinalização sonora por meio de um buzzer ativo conectado à interface GPIO da Raspberry Pi, distinguindo o término da inicialização do sistema (três bipes curtos) da interrupção do serviço ou desligamento da placa (um bipe longo).

---

## 2. Arquitetura e Hardware

* **Plataforma:** Raspberry Pi (Raspberry Pi OS)
* **Periférico:** Módulo Buzzer Ativo com acionamento em nível lógico baixo (*Active Low*)
* **Conexão Física:**
  * **Sinal:** `GPIO 2` (numeração BCM) / Pino físico 3
  * **Alimentação:** VCC e GND da barra de pinos da Raspberry Pi

Como o módulo opera em lógica invertida (`LIGA = GPIO.LOW` e `DESLIGA = GPIO.HIGH`), o pino é inicializado explicitamente em nível alto (`initial=DESLIGA`). A função `GPIO.cleanup()` foi omitida intencionalmente ao término dos scripts para evitar que o pino retorne ao estado de alta impedância e acione o buzzer de forma indesejada.

---

## 3. Descrição dos Arquivos

```text
.
├── buzzer.py          # Rotina de sinalização de inicialização (3 bipes curtos)
├── buzzer_stop.py     # Rotina de sinalização de encerramento (1 bipe longo)
├── buzzer.service     # Arquivo de definição do serviço para o systemd
└── README.md          # Documentação do Checkpoint 1
