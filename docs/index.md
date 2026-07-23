<!-- ---
layout: home
hero:
  name: Esen Theme Documentation
  text: English / 中文
  actions:
    - theme: brand
      text: English
      link: /en/
    - theme: alt
      text: 中文
      link: /zh/
--- -->
<script setup>
import { onMounted } from 'vue'

onMounted(() => {
  window.location.replace('/en/getting-started')
})
</script>
