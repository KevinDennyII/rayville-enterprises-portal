# Rayville Enterprises Portal - Design Guidelines

## Design Approach: Hybrid Professional System
**Selected Approach**: Clean corporate design system with subtle local branding elements
**Justification**: Professional service portal requiring trust and efficiency while maintaining local Baltimore connection

## Core Design Elements

### Color Palette
**Primary Brand**: 220 25% 25% (Professional navy)
**Secondary**: 220 15% 55% (Medium gray-blue)
**Background Light**: 220 10% 98% (Off-white)
**Background Dark**: 220 20% 12% (Dark navy)
**Accent**: 15 75% 50% (Warm orange - subtle Baltimore brick reference)

### Typography
**Primary**: Inter (headings, body text)
**Secondary**: Source Sans Pro (supporting text)
**Hierarchy**: text-4xl/3xl/2xl/xl/lg/base/sm

### Layout System
**Spacing Units**: Tailwind 3, 6, 8, 12, 16, 24
**Grid**: 12-column responsive grid
**Containers**: max-w-7xl with px-6 padding

### Component Library
**Navigation**: Clean horizontal nav with business unit dropdowns
**Cards**: Elevated service cards with subtle shadows
**Forms**: Professional contact forms with proper validation states
**Buttons**: Primary (filled), Secondary (outline), Text variants
**Footer**: Sticky footer with business info and quick links

## Page Structure

### Hero Section
**Layout**: Split-screen design
- Left: Company branding, tagline, primary CTA
- Right: Baltimore monument image (filtered/overlay for text contrast)
**Height**: 70vh minimum
**Content**: "Professional Property & Inspection Services" messaging

### Business Units Section
**Layout**: Two-column card layout
- Property Management card with relevant services
- Home/Lead Inspections card with certifications
**Visual**: Icon-driven with clean typography

### Trust Indicators
**Content**: Years of service, certifications, local presence
**Layout**: Horizontal stats bar or grid

### Contact Section
**Layout**: Form + contact information side-by-side
**Integration**: Direct connection to business units

## Images
**Hero Image**: Baltimore monument (Washington Monument) - filtered with dark overlay (opacity 40%) for text contrast
**Service Images**: Professional property and inspection photography - use as card backgrounds with overlays
**Team Photos**: Optional professional headshots in about section
**Certification Badges**: Display relevant industry certifications

## Technical Requirements
**CSS Organization**: Josh Comeau methodology with utility-first approach
**Sticky Footer**: Implemented with flexbox min-height structure
**Responsive**: Mobile-first design with breakpoints at sm/md/lg/xl
**Contrast**: WCAG AA compliant throughout
**Performance**: Optimized images with proper loading states

## Interactive Elements
**Navigation**: Smooth scrolling between sections
**Cards**: Subtle hover elevations (shadow increase)
**Buttons**: Built-in Tailwind hover/focus states
**Forms**: Real-time validation feedback

This design balances professional corporate aesthetics with local Baltimore identity, ensuring trust and credibility for both business units while maintaining modern usability standards.