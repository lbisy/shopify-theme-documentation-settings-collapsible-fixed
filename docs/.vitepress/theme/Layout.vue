<script setup>
import DefaultTheme from 'vitepress/theme'
import { nextTick, onBeforeUnmount, onMounted, ref, watch } from 'vue'
import { useRoute } from 'vitepress'

const DefaultLayout = DefaultTheme.Layout
const route = useRoute()

const isOpen = ref(false)
const imageSource = ref('')
const imageAlt = ref('')
const dialogLabel = ref('')
const closeLabel = ref('')
const closeButton = ref(null)

let lastFocusedElement = null
let previousBodyOverflow = ''
let imageObserver = null

const imageSelector = '.vp-doc img:not([data-no-zoom])'

function usesChineseLabels() {
  return document.documentElement.lang.toLowerCase().startsWith('zh')
}

function enhanceImage(image) {
  if (!(image instanceof HTMLImageElement)) return
  if (image.closest('a') || image.dataset.imageZoomReady === 'true') return

  const alt = image.getAttribute('alt')?.trim() || ''
  const label = usesChineseLabels()
    ? `放大查看图片${alt ? `：${alt}` : ''}`
    : `View enlarged image${alt ? `: ${alt}` : ''}`

  image.dataset.imageZoomReady = 'true'
  image.classList.add('docs-image-zoom-trigger')
  image.tabIndex = 0
  image.setAttribute('role', 'button')
  image.setAttribute('aria-label', label)
}

function enhanceImagesIn(node) {
  if (!(node instanceof Element)) return

  if (node.matches(imageSelector)) enhanceImage(node)
  node.querySelectorAll(imageSelector).forEach(enhanceImage)
}

function getZoomableImage(target) {
  if (!(target instanceof HTMLImageElement)) return null
  if (!target.matches(imageSelector) || target.closest('a')) return null
  return target
}

function openLightbox(image) {
  const alt = image.getAttribute('alt')?.trim() || ''
  const isChinese = usesChineseLabels()

  const activeElement = document.activeElement
  lastFocusedElement = activeElement instanceof HTMLElement && activeElement !== document.body
    ? activeElement
    : image
  imageSource.value = image.currentSrc || image.src
  imageAlt.value = alt
  dialogLabel.value = isChinese ? '图片放大预览' : 'Enlarged image preview'
  closeLabel.value = isChinese ? '关闭图片预览' : 'Close image preview'

  previousBodyOverflow = document.body.style.overflow
  document.body.style.overflow = 'hidden'
  isOpen.value = true

  nextTick(() => closeButton.value?.focus())
}

function closeLightbox({ restoreFocus = true } = {}) {
  if (!isOpen.value) return

  isOpen.value = false
  document.body.style.overflow = previousBodyOverflow

  const focusTarget = lastFocusedElement
  lastFocusedElement = null

  if (restoreFocus && focusTarget?.isConnected) {
    nextTick(() => focusTarget.focus())
  }
}

function handleDocumentClick(event) {
  const image = getZoomableImage(event.target)
  if (image) openLightbox(image)
}

function handleDocumentKeydown(event) {
  if (isOpen.value) {
    if (event.key === 'Escape') {
      event.preventDefault()
      closeLightbox()
    } else if (event.key === 'Tab') {
      event.preventDefault()
      closeButton.value?.focus()
    }
    return
  }

  if (event.key !== 'Enter' && event.key !== ' ') return

  const image = getZoomableImage(event.target)
  if (!image) return

  event.preventDefault()
  openLightbox(image)
}

watch(
  () => route.path,
  () => {
    closeLightbox({ restoreFocus: false })
    nextTick(() => enhanceImagesIn(document.body))
  }
)

onMounted(() => {
  enhanceImagesIn(document.body)

  imageObserver = new MutationObserver((mutations) => {
    for (const mutation of mutations) {
      mutation.addedNodes.forEach(enhanceImagesIn)
    }
  })
  imageObserver.observe(document.body, { childList: true, subtree: true })

  document.addEventListener('click', handleDocumentClick)
  document.addEventListener('keydown', handleDocumentKeydown)
})

onBeforeUnmount(() => {
  imageObserver?.disconnect()
  document.removeEventListener('click', handleDocumentClick)
  document.removeEventListener('keydown', handleDocumentKeydown)
  document.body.style.overflow = previousBodyOverflow
})
</script>

<template>
  <DefaultLayout />

  <Teleport to="body">
    <Transition name="docs-image-lightbox">
      <div
        v-if="isOpen"
        class="docs-image-lightbox"
        role="dialog"
        aria-modal="true"
        :aria-label="dialogLabel"
        :aria-describedby="imageAlt ? 'docs-image-lightbox-caption' : undefined"
        @click.self="closeLightbox()"
      >
        <button
          ref="closeButton"
          class="docs-image-lightbox__close"
          type="button"
          :aria-label="closeLabel"
          @click="closeLightbox()"
        >
          <span aria-hidden="true">×</span>
        </button>

        <img
          class="docs-image-lightbox__image"
          :src="imageSource"
          :alt="imageAlt"
        >

        <p
          v-if="imageAlt"
          id="docs-image-lightbox-caption"
          class="docs-image-lightbox__caption"
        >
          {{ imageAlt }}
        </p>
      </div>
    </Transition>
  </Teleport>
</template>
