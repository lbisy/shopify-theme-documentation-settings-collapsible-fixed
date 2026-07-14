import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'Shopify Theme Documentation',
  description: 'Bilingual Shopify theme user documentation',
  cleanUrls: true,

  locales: {
    en: { label: 'English', lang: 'en', link: '/en/' },
    zh: { label: '中文', lang: 'zh-CN', link: '/zh/' }
  },

  themeConfig: {
    search: { provider: 'local' },
    i18nRouting: true,

    locales: {
      en: {
        label: 'English',
        langMenuLabel: 'Languages',
        returnToTopLabel: 'Return to top',
        sidebarMenuLabel: 'Menu',
        darkModeSwitchLabel: 'Appearance',
        outlineTitle: 'On this page',
        docFooter: { prev: 'Previous page', next: 'Next page' }
      },
      zh: {
        label: '中文',
        langMenuLabel: '语言',
        returnToTopLabel: '返回顶部',
        sidebarMenuLabel: '菜单',
        darkModeSwitchLabel: '外观',
        outlineTitle: '本页目录',
        docFooter: { prev: '上一页', next: '下一页' }
      }
    },

    sidebar: {
      '/en/': [
        {
          text: 'Guide',
          items: [
              { text: "Getting Started", link: "/en/getting-started" },
              { text: "Installation", link: "/en/installation" },
              { text: "Theme Editor", link: "/en/theme-editor" },
              {
                text: 'Global Theme Settings',
                collapsed: true,
                items: [
                  { text: 'Settings Overview', link: '/en/theme-settings' },
                  { text: 'Logo', link: '/en/settings/logo' },
                  { text: 'Typography', link: '/en/settings/typography' },
                  { text: 'Layout', link: '/en/settings/layout' },
                  { text: 'Colors', link: '/en/settings/colors' },
                  { text: 'Input', link: '/en/settings/input' },
                  { text: 'Button', link: '/en/settings/button' },
                  { text: 'Dialog', link: '/en/settings/dialog' },
                  { text: 'Product cards', link: '/en/settings/product-cards' },
                  { text: 'Toast', link: '/en/settings/toast' },
                  { text: 'Cart', link: '/en/settings/cart' },
                  { text: 'Search', link: '/en/settings/search' },
                  { text: 'Animations', link: '/en/settings/animations' },
                  { text: 'Focus', link: '/en/settings/focus' },
                  { text: 'Social icon', link: '/en/settings/social-icon' }
                ]
              },
              { text: "Header & Footer", link: "/en/header-footer" },
              { text: "Product Pages", link: "/en/product-pages" },
              { text: "Collection Pages", link: "/en/collection-pages" },
              { text: "Cart & Search", link: "/en/cart-search" },
              { text: "Blog & Articles", link: "/en/blog-pages" },
              { text: "About & Contact", link: "/en/about-contact" },
              { text: "FAQ", link: "/en/faq" },
              { text: "Support & Updates", link: "/en/support" }
          ]
        },
        {
          text: 'Homepage Sections',
          collapsed: false,
          items: [
              { text: "404 Page", link: "/en/sections/404" },
              { text: "About Statistics", link: "/en/sections/about-stats" },
              { text: "Before & After Comparison", link: "/en/sections/before-after-comparison" },
              { text: "Blog Stories", link: "/en/sections/blog-stories" },
              { text: "Brand Statement", link: "/en/sections/brand-statement" },
              { text: "Cart Overlay", link: "/en/sections/cart-overlay" },
              { text: "Category Grid", link: "/en/sections/category-grid" },
              { text: "Collections Grid", link: "/en/sections/collections" },
              { text: "Custom Liquid", link: "/en/sections/custom-liquid" },
              { text: "Featured Product", link: "/en/sections/featured-product" },
              { text: "Featured Products", link: "/en/sections/featured-products" },
              { text: "Google Map", link: "/en/sections/google-map" },
              { text: "Icon with Text", link: "/en/sections/icon-with-text" },
              { text: "Newsletter Banner", link: "/en/sections/newsletter-banner" },
              { text: "Newsletter Overlay", link: "/en/sections/newsletter-overlay" },
              { text: "Page", link: "/en/sections/page" },
              { text: "Password Footer", link: "/en/sections/password-footer" },
              { text: "Password Header", link: "/en/sections/password-header" },
              { text: "Password Page", link: "/en/sections/password" },
              { text: "Philosophy Section", link: "/en/sections/philosophy-section" },
              { text: "Pickup Availability", link: "/en/sections/pickup-availability" },
              { text: "Product Comparison Table", link: "/en/sections/product-comparison-table" },
              { text: "Product Recommendations", link: "/en/sections/product-recommendations" },
              { text: "Promise Section", link: "/en/sections/promise-section" },
              { text: "Promotion Banner", link: "/en/sections/promo-bannder" },
              { text: "Promotion Countdown", link: "/en/sections/promotion-countdown" },
              { text: "Routine Showcase", link: "/en/sections/routine-showcase" },
              { text: "Scrolling Categories", link: "/en/sections/scroll-categories" },
              { text: "Scrolling Icons with Text", link: "/en/sections/scrolling-icon-with-text" },
              { text: "Search Overlay", link: "/en/sections/search-overlay" },
              { text: "Slideshow", link: "/en/sections/slides-show" },
              { text: "Featured Testimonials", link: "/en/sections/testimonial-featured" },
              { text: "Video Banner", link: "/en/sections/video-banner" }
          ]
        }
      ],
      '/zh/': [
        {
          text: '使用指南',
          items: [
              { text: "开始使用", link: "/zh/getting-started" },
              { text: "安装主题", link: "/zh/installation" },
              { text: "主题编辑器", link: "/zh/theme-editor" },
              {
                text: '全局主题设置',
                collapsed: true,
                items: [
                  { text: '设置概览', link: '/zh/theme-settings' },
                  { text: 'Logo', link: '/zh/settings/logo' },
                  { text: 'Typography', link: '/zh/settings/typography' },
                  { text: 'Layout', link: '/zh/settings/layout' },
                  { text: 'Colors', link: '/zh/settings/colors' },
                  { text: 'Input', link: '/zh/settings/input' },
                  { text: 'Button', link: '/zh/settings/button' },
                  { text: 'Dialog', link: '/zh/settings/dialog' },
                  { text: 'Product cards', link: '/zh/settings/product-cards' },
                  { text: 'Toast', link: '/zh/settings/toast' },
                  { text: 'Cart', link: '/zh/settings/cart' },
                  { text: 'Search', link: '/zh/settings/search' },
                  { text: 'Animations', link: '/zh/settings/animations' },
                  { text: 'Focus', link: '/zh/settings/focus' },
                  { text: 'Social icon', link: '/zh/settings/social-icon' }
                ]
              },
              { text: "页眉与页脚", link: "/zh/header-footer" },
              { text: "商品页面", link: "/zh/product-pages" },
              { text: "集合页面", link: "/zh/collection-pages" },
              { text: "购物车与搜索", link: "/zh/cart-search" },
              { text: "博客与文章", link: "/zh/blog-pages" },
              { text: "关于我们与联系我们", link: "/zh/about-contact" },
              { text: "常见问题", link: "/zh/faq" },
              { text: "技术支持与更新", link: "/zh/support" }
          ]
        },
        {
          text: '首页模块',
          collapsed: false,
          items: [
              { text: "404 页面", link: "/zh/sections/404" },
              { text: "关于我们数据", link: "/zh/sections/about-stats" },
              { text: "前后对比", link: "/zh/sections/before-after-comparison" },
              { text: "博客故事", link: "/zh/sections/blog-stories" },
              { text: "品牌宣言", link: "/zh/sections/brand-statement" },
              { text: "购物车弹层", link: "/zh/sections/cart-overlay" },
              { text: "分类网格", link: "/zh/sections/category-grid" },
              { text: "集合网格", link: "/zh/sections/collections" },
              { text: "自定义 Liquid", link: "/zh/sections/custom-liquid" },
              { text: "精选单品", link: "/zh/sections/featured-product" },
              { text: "精选商品列表", link: "/zh/sections/featured-products" },
              { text: "Google 地图", link: "/zh/sections/google-map" },
              { text: "图标与文字", link: "/zh/sections/icon-with-text" },
              { text: "邮件订阅横幅", link: "/zh/sections/newsletter-banner" },
              { text: "邮件订阅弹层", link: "/zh/sections/newsletter-overlay" },
              { text: "普通页面", link: "/zh/sections/page" },
              { text: "密码页页脚", link: "/zh/sections/password-footer" },
              { text: "密码页页眉", link: "/zh/sections/password-header" },
              { text: "密码页面", link: "/zh/sections/password" },
              { text: "品牌理念", link: "/zh/sections/philosophy-section" },
              { text: "到店取货状态", link: "/zh/sections/pickup-availability" },
              { text: "商品对比表", link: "/zh/sections/product-comparison-table" },
              { text: "商品推荐", link: "/zh/sections/product-recommendations" },
              { text: "品牌承诺", link: "/zh/sections/promise-section" },
              { text: "促销横幅", link: "/zh/sections/promo-bannder" },
              { text: "促销倒计时", link: "/zh/sections/promotion-countdown" },
              { text: "使用流程展示", link: "/zh/sections/routine-showcase" },
              { text: "滚动分类", link: "/zh/sections/scroll-categories" },
              { text: "滚动图标文字", link: "/zh/sections/scrolling-icon-with-text" },
              { text: "搜索弹层", link: "/zh/sections/search-overlay" },
              { text: "幻灯片轮播", link: "/zh/sections/slides-show" },
              { text: "客户评价", link: "/zh/sections/testimonial-featured" },
              { text: "视频横幅", link: "/zh/sections/video-banner" }
          ]
        }
      ]
    }
  }
})
