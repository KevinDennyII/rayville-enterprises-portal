# Design Guidelines for Rayville Enterprises Business Portal

## Design Approach
**Selected Approach:** Design System (Function-Focused)
Using a refined Material Design approach for professional business applications, emphasizing clean hierarchy and efficient information display.

## Core Design Elements

### A. Color Palette
**Primary Colors:**
- Light mode: 220 15% 25% (deep navy)
- Dark mode: 220 30% 85% (light blue-gray)

**Accent Colors:**
- Professional blue: 210 90% 45%
- Success green: 140 70% 40%

### B. Typography
**Font Stack:** Inter via Google Fonts
- Headings: 600 weight, sizes from text-xl to text-3xl
- Body text: 400 weight, text-base
- Subtext: 500 weight, text-sm

### C. Layout System
**Spacing Primitives:** Use Tailwind units of 2, 4, 6, and 8
- Component spacing: p-4, p-6
- Section gaps: space-y-6, space-y-8
- Grid gaps: gap-4, gap-6

### D. Component Library

**Header:**
- Fixed height with logo left-aligned
- Minimal padding (py-2, px-4)
- Clean border-bottom with subtle shadow

**Business Service Cards:**
- Card grid: 2-3 columns on desktop, 1 on mobile
- Compact card design with icon, title, brief description
- Hover states with subtle elevation
- Clean borders, rounded corners (rounded-lg)

**Main Content Area:**
- **Reduced title spacing:** Use py-4 instead of py-8 around main title
- Container max-width for readability
- Proper content hierarchy with consistent spacing

**Sticky Footer:**
- Minimal height, essential contact info only
- Subtle background differentiation
- Proper z-index for overlay behavior

### E. Professional Business Card Design
Each service card includes:
- Icon placeholder (use Heroicons for consistency)
- Service title (text-lg, font-semibold)
- 2-3 line description (text-sm, text-gray-600)
- Optional "Learn More" subtle link

## Images Section
**No large hero image required** - this is a focused business portal prioritizing quick service access over visual marketing.

**Service Card Icons:** Use Heroicons library for consistent professional iconography (building, chart-bar, users, etc.)

**Logo Placement:** Company logo in header, sized appropriately for professional context (h-8 to h-10)

## Key Implementation Notes
- Prioritize content density over excessive whitespace
- Use consistent card shadows for depth hierarchy
- Implement responsive grid that maintains card proportions
- Ensure footer remains functional and unobtrusive
- Focus on fast loading and clean information architecture

This design emphasizes professional efficiency while maintaining visual appeal appropriate for a business portal.