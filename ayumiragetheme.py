def write_gtk3_css(
    color0,
    color1,
    color2,
    color3,
    color4,
    color5,
    color6,
    color7,
    color8,
    color9,
    color10,
    color11,
    color12,
    color13,
    color14,
    color15,
):
    with open(
        "/home/x1carbon/.themes/Ayu-Mirage-Dark/gtk-3.0/gtk.css", "w"
    ) as rofi_file:
        rofi_file_data = (
            """
* {
  background-clip: padding-box;
  -GtkToolButton-icon-spacing: 4;
  -GtkTextView-error-underline-color: #FC4138;
  -GtkScrolledWindow-scrollbar-spacing: 0;
  -GtkToolItemGroup-expander-size: 11;
  -GtkWidget-text-handle-width: 20;
  -GtkWidget-text-handle-height: 20;
  -GtkDialog-button-spacing: 4;
  -GtkDialog-action-area-border: 0;
  outline-color: alpha(currentColor,0.3);
  outline-style: dashed;
  outline-offset: -3px;
  outline-width: 1px;
  -gtk-outline-radius: 2px; }

.background {
  color: """
            + color1
            + """;
  background-color: """
            + color0
            + """; }

*:disabled {
  -gtk-icon-effect: dim; }

.gtkstyle-fallback {
  background-color: """
            + color6
            + """;
  color: """
            + color1
            + """; }
  .gtkstyle-fallback:hover {
    background-color: #333b4f;
    color: """
            + color1
            + """; }
  .gtkstyle-fallback:active {
    background-color: #0b0d11;
    color: """
            + color1
            + """; }
  .gtkstyle-fallback:disabled {
    background-color: #232936;
    color: rgba(203, 204, 198, 0.45); }
  .gtkstyle-fallback:selected {
    background-color: """
            + color4
            + """;
    color: """
            + color1
            + """; }

.view, iconview,
.view text,
iconview text,
textview text {
  color: """
            + color1
            + """;
  background-color: """
            + color14
            + """; }
  .view:selected, iconview:selected, .view:selected:focus, iconview:selected:focus,
  .view text:selected,
  iconview text:selected,
  textview text:selected,
  .view text:selected:focus,
  iconview text:selected:focus,
  textview text:selected:focus {
    border-radius: 2px; }

textview border {
  background-color: """
            + color3
            + """; }

rubberband, flowbox rubberband, treeview.view rubberband, .content-view rubberband,
.rubberband {
  border: 1px solid #212c3a;
  background-color: rgba(33, 44, 58, 0.2); }

flowbox flowboxchild {
  padding: 3px;
  border-radius: 2px; }
  flowbox flowboxchild:selected {
    outline-offset: -2px; }

label.separator, popover label.separator,
popover.background label.separator {
  color: """
            + color1
            + """; }

label selection {
  color: """
            + color1
            + """;
  background-color: """
            + color4
            + """; }

label:disabled {
  color: rgba(203, 204, 198, 0.45); }

.dim-label, label.separator, popover label.separator,
popover.background label.separator, headerbar .subtitle, .titlebar:not(headerbar) .subtitle {
  opacity: 0.55; }

assistant .sidebar {
  background-color: """
            + color2
            + """;
  border-top: 1px solid #13161d; }

assistant.csd .sidebar {
  border-top-style: none; }

assistant .sidebar label {
  padding: 6px 12px; }

assistant .sidebar label.highlight {
  background-color: """
            + color4
            + """;
  color: """
            + color1
            + """; }

textview {
  background-color: """
            + color2
            + """; }

popover.osd, popover.magnifier, .csd popover.osd, .csd popover.magnifier,
popover.background.osd,
popover.background.magnifier, .csd popover.background.osd, .csd popover.background.magnifier, .osd .scale-popup, .osd {
  color: """
            + color1
            + """;
  border: none;
  background-color: rgba(35, 40, 52, 0.95);
  background-clip: padding-box;
  box-shadow: none; }

@keyframes spin {
  to {
    -gtk-icon-transform: rotate(1turn); } }

spinner {
  background: none;
  opacity: 0;
  -gtk-icon-source: -gtk-icontheme("process-working-symbolic"); }
  spinner:checked {
    opacity: 1;
    animation: spin 1s linear infinite; }
    spinner:checked:disabled {
      opacity: 0.5; }

entry {
  min-height: 22px;
  border: 1px solid;
  padding: 2px 8px;
  caret-color: currentColor;
  border-radius: 3px;
  transition: all 200ms cubic-bezier(0.25, 0.46, 0.45, 0.94);
  color: """
            + color1
            + """;
  border-color: #13161d;
  background-color: """
            + color2
            + """; }
  entry.search {
    border-radius: 20px; }
  entry image {
    color: #a9aba9; }
    entry image.left {
      padding-left: 0;
      padding-right: 5px; }
    entry image.right {
      padding-right: 0;
      padding-left: 5px; }
  entry.flat, entry.flat:focus {
    min-height: 0;
    padding: 2px;
    background-image: none;
    border-color: transparent;
    border-radius: 0; }
  entry:focus {
    background-clip: border-box;
    color: """
            + color1
            + """;
    border-color: #13161d;
    background-color: """
            + color2
            + """;
    box-shadow: inset 1px 0 """
            + color4
            + """, inset -1px 0 """
            + color4
            + """, inset 0 1px """
            + color4
            + """, inset 0 -1px """
            + color4
            + """; }
  entry:disabled {
    color: rgba(203, 204, 198, 0.45);
    border-color: rgba(19, 22, 29, 0.55);
    background-color: rgba(35, 40, 52, 0.55); }
  entry.warning {
    color: white;
    border-color: #13161d;
    background-color: #9f5835; }
    entry.warning image {
      color: white; }
    entry.warning:focus {
      color: white;
      background-color: #F27835;
      box-shadow: none; }
    entry.warning selection, entry.warning selection:focus {
      background-color: white;
      color: #F27835; }
  entry.error {
    color: white;
    border-color: #13161d;
    background-color: #a53736; }
    entry.error image {
      color: white; }
    entry.error:focus {
      color: white;
      background-color: #FC4138;
      box-shadow: none; }
    entry.error selection, entry.error selection:focus {
      background-color: white;
      color: #FC4138; }
  entry.search-missing {
    color: white;
    border-color: #13161d;
    background-color: #a53736; }
    entry.search-missing image {
      color: white; }
    entry.search-missing:focus {
      color: white;
      background-color: #FC4138;
      box-shadow: none; }
    entry.search-missing selection, entry.search-missing selection:focus {
      background-color: white;
      color: #FC4138; }
  entry:drop(active):focus, entry:drop(active) {
    border-color: #F08437;
    box-shadow: none; }
  .osd entry {
    color: """
            + color1
            + """;
    border-color: rgba(10, 12, 15, 0.35);
    background-color: rgba(80, 92, 119, 0.35); }
    .osd entry image, .osd entry image:hover {
      color: inherit; }
    .osd entry:focus {
      color: """
            + color1
            + """;
      border-color: rgba(10, 12, 15, 0.35);
      background-color: """
            + color4
            + """; }
    .osd entry:disabled {
      color: rgba(203, 204, 198, 0.55);
      background-color: rgba(80, 92, 119, 0.2); }
    .osd entry selection:focus, .osd entry selection {
      color: """
            + color4
            + """;
      background-color: """
            + color1
            + """; }
  entry progress {
    margin: 0 -6px;
    border-radius: 0;
    border-width: 0 0 2px;
    border-color: """
            + color4
            + """;
    border-style: solid;
    background-image: none;
    background-color: transparent;
    box-shadow: none; }

treeview entry.flat, treeview entry {
  border-radius: 0;
  background-image: none;
  background-color: """
            + color2
            + """; }
  treeview entry.flat:focus, treeview entry:focus {
    border-color: """
            + color4
            + """; }

@keyframes needs_attention {
  from {
    background-image: -gtk-gradient(radial, center center, 0, center center, 0.01, to("""
            + color4
            + """), to(transparent)); }
  to {
    background-image: -gtk-gradient(radial, center center, 0, center center, 0.5, to("""
            + color4
            + """), to(transparent)); } }

button {
  min-height: 22px;
  min-width: 20px;
  transition: all 200ms cubic-bezier(0.25, 0.46, 0.45, 0.94);
  border: 1px solid;
  border-radius: 3px;
  padding: 2px 6px;
  color: """
            + color1
            + """;
  border-color: #13161d;
  background-color: """
            + color5
            + """; }
  button separator {
    margin: 4px 1px; }
  button.flat, button.sidebar-button {
    border-color: transparent;
    background-color: transparent;
    background-image: none;
    transition: none; }
    button.flat:hover, button.sidebar-button:hover {
      transition: all 200ms cubic-bezier(0.25, 0.46, 0.45, 0.94);
      transition-duration: 350ms; }
      button.flat:hover:active, button.sidebar-button:hover:active {
        transition: all 200ms cubic-bezier(0.25, 0.46, 0.45, 0.94); }
  button:hover {
    color: """
            + color1
            + """;
    border-color: #13161d;
    background-color: #313849;
    -gtk-icon-effect: highlight; }
  button:active, button:checked {
    color: """
            + color1
            + """;
    border-color: #13161d;
    background-color: """
            + color4
            + """;
    background-clip: padding-box;
    transition-duration: 50ms; }
    button:active:not(:disabled) label:disabled, button:checked:not(:disabled) label:disabled {
      color: inherit;
      opacity: 0.6; }
  button:active {
    color: """
            + color1
            + """; }
  button:active:hover, button:checked {
    color: """
            + color1
            + """; }
  button.flat:disabled, button.sidebar-button:disabled {
    border-color: transparent;
    background-color: transparent;
    background-image: none; }
  button:disabled {
    border-color: rgba(19, 22, 29, 0.55);
    background-color: rgba(39, 45, 58, 0.55); }
    button:disabled label, button:disabled {
      color: rgba(203, 204, 198, 0.45); }
    button:disabled:active, button:disabled:checked {
      border-color: rgba(52, 69, 90, 0.75);
      background-color: rgba(52, 69, 90, 0.75);
      opacity: 0.6; }
      button:disabled:active label, button:disabled:active, button:disabled:checked label, button:disabled:checked {
        color: rgba(203, 204, 198, 0.8); }
  button.image-button {
    min-width: 24px;
    padding-left: 5px;
    padding-right: 5px; }
  button.text-button {
    padding-left: 12px;
    padding-right: 12px; }
  button.text-button.image-button {
    padding-left: 5px;
    padding-right: 5px; }
    button.text-button.image-button label:first-child {
      padding-left: 8px;
      padding-right: 2px; }
    button.text-button.image-button label:last-child {
      padding-right: 8px;
      padding-left: 2px; }
    button.text-button.image-button label:only-child {
      padding-left: 8px;
      padding-right: 8px; }
    button.text-button.image-button.popup {
      padding-right: 8px;
      padding-left: 8px; }
  button:drop(active), combobox:drop(active) button.combo {
    color: #F08437;
    border-color: #F08437;
    box-shadow: none; }
  button.osd {
    color: """
            + color1
            + """;
    background-color: rgba(35, 40, 52, 0.95);
    border-color: rgba(19, 21, 28, 0.95); }
    button.osd.image-button {
      padding: 0;
      min-height: 36px;
      min-width: 36px; }
    button.osd:hover {
      color: """
            + color4
            + """; }
    button.osd:active, button.osd:checked {
      color: """
            + color1
            + """;
      border-color: rgba(10, 12, 15, 0.35);
      background-color: """
            + color4
            + """; }
    button.osd:disabled {
      color: #555960;
      border-color: rgba(10, 12, 15, 0.35);
      background-color: rgba(80, 92, 119, 0.2); }
  .osd button {
    color: """
            + color1
            + """;
    border-color: rgba(10, 12, 15, 0.35);
    background-color: rgba(80, 92, 119, 0.35); }
    .osd button:hover {
      color: """
            + color1
            + """;
      border-color: rgba(10, 12, 15, 0.35);
      background-color: rgba(95, 108, 140, 0.45); }
    .osd button:active, .osd button:checked {
      background-clip: padding-box;
      color: """
            + color1
            + """;
      border-color: rgba(10, 12, 15, 0.35);
      background-color: """
            + color4
            + """; }
    .osd button:disabled {
      color: #555960;
      border-color: rgba(10, 12, 15, 0.35);
      background-color: rgba(80, 92, 119, 0.2); }
    .osd button.flat, .osd button.sidebar-button {
      border-color: transparent;
      background-color: transparent;
      background-image: none;
      box-shadow: none; }
      .osd button.flat:hover, .osd button.sidebar-button:hover {
        color: """
            + color1
            + """;
        border-color: rgba(10, 12, 15, 0.35);
        background-color: rgba(95, 108, 140, 0.45); }
      .osd button.flat:disabled, .osd button.sidebar-button:disabled {
        color: #555960;
        border-color: rgba(10, 12, 15, 0.35);
        background-color: rgba(80, 92, 119, 0.2);
        background-image: none; }
      .osd button.flat:active, .osd button.sidebar-button:active, .osd button.flat:checked, .osd button.sidebar-button:checked {
        color: """
            + color1
            + """;
        border-color: rgba(10, 12, 15, 0.35);
        background-color: """
            + color4
            + """; }
  .osd .linked:not(.vertical):not(.path-bar) > button:hover:not(:checked):not(:active):not(:only-child),
  .osd .linked:not(.vertical):not(.path-bar) > button:hover:not(:checked):not(:active) + button:not(:checked):not(:active) {
    box-shadow: none; }
  button.suggested-action {
    background-clip: border-box;
    color: white;
    background-color: #4DADD4;
    border-color: #4DADD4; }
    button.suggested-action.flat, button.suggested-action.sidebar-button {
      border-color: transparent;
      background-color: transparent;
      background-image: none;
      color: #4DADD4; }
    button.suggested-action:hover {
      background-clip: border-box;
      color: white;
      background-color: #76c0de;
      border-color: #76c0de; }
    button.suggested-action:active, button.suggested-action:checked {
      background-clip: border-box;
      color: white;
      background-color: #2e96c0;
      border-color: #2e96c0; }
    button.suggested-action.flat:disabled, button.suggested-action.sidebar-button:disabled {
      border-color: transparent;
      background-color: transparent;
      background-image: none;
      color: rgba(203, 204, 198, 0.45); }
    button.suggested-action:disabled {
      border-color: rgba(19, 22, 29, 0.55);
      background-color: rgba(39, 45, 58, 0.55); }
      button.suggested-action:disabled label, button.suggested-action:disabled {
        color: rgba(203, 204, 198, 0.45); }
  button.destructive-action {
    background-clip: border-box;
    color: white;
    background-color: #F04A50;
    border-color: #F04A50; }
    button.destructive-action.flat, button.destructive-action.sidebar-button {
      border-color: transparent;
      background-color: transparent;
      background-image: none;
      color: #F04A50; }
    button.destructive-action:hover {
      background-clip: border-box;
      color: white;
      background-color: #f4797e;
      border-color: #f4797e; }
    button.destructive-action:active, button.destructive-action:checked {
      background-clip: border-box;
      color: white;
      background-color: #ec1b22;
      border-color: #ec1b22; }
    button.destructive-action.flat:disabled, button.destructive-action.sidebar-button:disabled {
      border-color: transparent;
      background-color: transparent;
      background-image: none;
      color: rgba(203, 204, 198, 0.45); }
    button.destructive-action:disabled {
      border-color: rgba(19, 22, 29, 0.55);
      background-color: rgba(39, 45, 58, 0.55); }
      button.destructive-action:disabled label, button.destructive-action:disabled {
        color: rgba(203, 204, 198, 0.45); }
  .stack-switcher > button {
    outline-offset: -3px; }
    .stack-switcher > button > label {
      padding-left: 6px;
      padding-right: 6px; }
    .stack-switcher > button > image {
      padding-left: 6px;
      padding-right: 6px;
      padding-top: 3px;
      padding-bottom: 3px; }
    .stack-switcher > button.text-button {
      padding-left: 10px;
      padding-right: 10px; }
    .stack-switcher > button.image-button {
      padding-left: 2px;
      padding-right: 2px; }
    .stack-switcher > button.needs-attention:active > label, .stack-switcher > button.needs-attention:active > image, .stack-switcher > button.needs-attention:checked > label, .stack-switcher > button.needs-attention:checked > image {
      animation: none;
      background-image: none; }
  .stack-switcher > button.needs-attention > label, .stack-switcher > button.needs-attention > image, button stacksidebar row.needs-attention > label, stacksidebar button row.needs-attention > label {
    animation: needs_attention 150ms ease-in;
    background-image: -gtk-gradient(radial, center center, 0, center center, 0.5, to("""
            + color4
            + """), to(transparent));
    background-size: 6px 6px, 6px 6px;
    background-repeat: no-repeat;
    background-position: right 3px, right 2px; }
    .stack-switcher > button.needs-attention > label:dir(rtl), .stack-switcher > button.needs-attention > image:dir(rtl), button stacksidebar row.needs-attention > label:dir(rtl), stacksidebar button row.needs-attention > label:dir(rtl) {
      background-position: left 3px, left 2px; }
  button.font separator, button.file separator {
    background-color: transparent; }
  .inline-toolbar button, .inline-toolbar button:backdrop {
    border-radius: 2px;
    border-width: 1px; }

.inline-toolbar toolbutton > button {
  color: """
            + color1
            + """;
  border-color: #13161d;
  background-color: """
            + color5
            + """; }
  .inline-toolbar toolbutton > button:hover {
    color: """
            + color1
            + """;
    border-color: #13161d;
    background-color: #313849; }
  .inline-toolbar toolbutton > button:active, .inline-toolbar toolbutton > button:checked {
    color: """
            + color1
            + """;
    border-color: #13161d;
    background-color: """
            + color4
            + """; }
  .inline-toolbar toolbutton > button:disabled {
    border-color: rgba(19, 22, 29, 0.55);
    background-color: rgba(39, 45, 58, 0.55); }
    .inline-toolbar toolbutton > button:disabled label, .inline-toolbar toolbutton > button:disabled {
      color: rgba(203, 204, 198, 0.45); }
  .inline-toolbar toolbutton > button:disabled:active, .inline-toolbar toolbutton > button:disabled:checked {
    border-color: rgba(52, 69, 90, 0.75);
    background-color: rgba(52, 69, 90, 0.75);
    opacity: 0.6; }
    .inline-toolbar toolbutton > button:disabled:active label, .inline-toolbar toolbutton > button:disabled:active, .inline-toolbar toolbutton > button:disabled:checked label, .inline-toolbar toolbutton > button:disabled:checked {
      color: rgba(203, 204, 198, 0.8); }

.linked:not(.vertical):not(.path-bar) > entry + entry {
  border-left-color: rgba(19, 22, 29, 0.3); }

.linked:not(.vertical):not(.path-bar) > entry.error + entry,
.linked:not(.vertical):not(.path-bar) > entry + entry.error {
  border-left-color: rgba(19, 22, 29, 0.3); }

.linked:not(.vertical):not(.path-bar) > entry.warning + entry,
.linked:not(.vertical):not(.path-bar) > entry + entry.warning {
  border-left-color: rgba(19, 22, 29, 0.3); }

.linked:not(.vertical):not(.path-bar) > entry.error + entry.warning,
.linked:not(.vertical):not(.path-bar) > entry.warning + entry.error {
  border-left-color: rgba(19, 22, 29, 0.3); }

.linked:not(.vertical):not(.path-bar) > entry + entry:focus:not(:last-child),
.linked:not(.vertical):not(.path-bar) > entry + entry:focus:last-child {
  border-left-color: #13161d; }

.linked:not(.vertical):not(.path-bar) > entry:focus:not(:only-child) + entry,
.linked:not(.vertical):not(.path-bar) > entry:focus:not(:only-child) + button,
.linked:not(.vertical):not(.path-bar) > entry:focus:not(:only-child) + combobox > box > button.combo {
  border-left-color: #13161d; }

.linked:not(.vertical):not(.path-bar) > entry + entry:drop(active):not(:last-child),
.linked:not(.vertical):not(.path-bar) > entry + entry:drop(active):last-child {
  border-left-color: #13161d; }

.linked:not(.vertical):not(.path-bar) > entry:drop(active):not(:only-child) + entry,
.linked:not(.vertical):not(.path-bar) > entry:drop(active):not(:only-child) + button,
.linked:not(.vertical):not(.path-bar) > entry:drop(active):not(:only-child) + combobox > box > button.combo {
  border-left-color: #13161d; }

.linked:not(.vertical):not(.path-bar) > entry + entry.warning:focus:not(:last-child),
.linked:not(.vertical):not(.path-bar) > entry + entry.warning:focus:last-child {
  border-left-color: #13161d; }

.linked:not(.vertical):not(.path-bar) > entry.warning:focus:not(:only-child) + entry,
.linked:not(.vertical):not(.path-bar) > entry.warning:focus:not(:only-child) + button,
.linked:not(.vertical):not(.path-bar) > entry.warning:focus:not(:only-child) + combobox > box > button.combo {
  border-left-color: #13161d; }

.linked:not(.vertical):not(.path-bar) > entry + entry.error:focus:not(:last-child),
.linked:not(.vertical):not(.path-bar) > entry + entry.error:focus:last-child {
  border-left-color: #13161d; }

.linked:not(.vertical):not(.path-bar) > entry.error:focus:not(:only-child) + entry,
.linked:not(.vertical):not(.path-bar) > entry.error:focus:not(:only-child) + button,
.linked:not(.vertical):not(.path-bar) > entry.error:focus:not(:only-child) + combobox > box > button.combo {
  border-left-color: #13161d; }

.linked:not(.vertical):not(.path-bar) > button:active + entry,
.linked:not(.vertical):not(.path-bar) > button:checked + entry {
  border-left-color: #13161d; }

.linked:not(.vertical):not(.path-bar) > button + button {
  border-left-style: none; }

.linked:not(.vertical):not(.path-bar) > button:not(:checked):not(:active):not(.suggested-action):not(.destructive-action):hover:not(:only-child),
.linked:not(.vertical):not(.path-bar) > button:not(:checked):not(:active):not(.suggested-action):not(.destructive-action):hover + button:not(:checked):not(:active):not(.suggested-action):not(.destructive-action) {
  box-shadow: inset 1px 0 #13161d; }

.linked:not(.vertical):not(.path-bar) > button:not(:checked):not(:active):not(.suggested-action):not(.destructive-action):disabled:not(:only-child),
.linked:not(.vertical):not(.path-bar) > button:not(:checked):not(:active):not(.suggested-action):not(.destructive-action):disabled + button:not(:checked):not(:active):not(.suggested-action):not(.destructive-action):not(:hover) {
  box-shadow: inset 1px 0 rgba(19, 22, 29, 0.5); }

.linked:not(.vertical):not(.path-bar) > button:active + button:not(:checked):not(:active):not(.suggested-action):not(.destructive-action):hover,
.linked:not(.vertical):not(.path-bar) > button:checked + button:not(:checked):not(:active):not(.suggested-action):not(.destructive-action):hover,
.linked:not(.vertical):not(.path-bar) > button.suggested-action + button:not(:checked):not(:active):not(.suggested-action):not(.destructive-action):hover,
.linked:not(.vertical):not(.path-bar) > button.destructive-action + button:not(:checked):not(:active):not(.suggested-action):not(.destructive-action):hover,
.linked:not(.vertical):not(.path-bar) > entry + button:not(:checked):not(:active):not(.suggested-action):not(.destructive-action):hover:not(:only-child),
.linked:not(.vertical):not(.path-bar) > button:not(:checked):not(:active):not(.suggested-action):not(.destructive-action):first-child:disabled,
.linked:not(.vertical):not(.path-bar) > button:not(:checked):not(:active):not(.suggested-action):not(.destructive-action):disabled + button:not(:checked):not(:active):not(.suggested-action):not(.destructive-action):disabled,
.linked:not(.vertical):not(.path-bar) > button:not(:checked):not(:active):not(.suggested-action):not(.destructive-action):first-child:hover,
.linked:not(.vertical):not(.path-bar) > button:active + button:not(:checked):not(:active):not(.suggested-action):not(.destructive-action):disabled,
.linked:not(.vertical):not(.path-bar) > button:checked + button:not(:checked):not(:active):not(.suggested-action):not(.destructive-action):disabled,
.linked:not(.vertical):not(.path-bar) > button.suggested-action + button:not(:checked):not(:active):not(.suggested-action):not(.destructive-action):disabled,
.linked:not(.vertical):not(.path-bar) > button.destructive-action + button:not(:checked):not(:active):not(.suggested-action):not(.destructive-action):disabled,
.linked:not(.vertical):not(.path-bar) > entry + button:not(:checked):not(:active):not(.suggested-action):not(.destructive-action):disabled:not(:only-child) {
  box-shadow: none; }

.linked:not(.vertical).path-bar > button + button {
  border-left-style: none; }

.linked:not(.vertical).path-bar > button:hover:not(:checked):not(:active):not(:only-child):hover {
  box-shadow: inset 1px 0 rgba(19, 22, 29, 0.5), inset -1px 0 rgba(19, 22, 29, 0.5); }

.linked:not(.vertical).path-bar > button:hover:not(:checked):not(:active):not(:only-child):first-child:hover {
  box-shadow: inset -1px 0 rgba(19, 22, 29, 0.5); }

.linked:not(.vertical).path-bar > button:hover:not(:checked):not(:active):not(:only-child):last-child:hover {
  box-shadow: inset 1px 0 rgba(19, 22, 29, 0.5); }

.linked.vertical > entry + entry {
  border-top-color: rgba(19, 22, 29, 0.3); }

.linked.vertical > entry.error + entry,
.linked.vertical > entry + entry.error {
  border-top-color: rgba(19, 22, 29, 0.3); }

.linked.vertical > entry.warning + entry,
.linked.vertical > entry + entry.warning {
  border-top-color: rgba(19, 22, 29, 0.3); }

.linked.vertical > entry.error + entry.warning,
.linked.vertical > entry.warning + entry.error {
  border-top-color: rgba(19, 22, 29, 0.3); }

.linked.vertical > entry + entry:focus:not(:last-child),
.linked.vertical > entry + entry:focus:last-child {
  border-top-color: #13161d; }

.linked.vertical > entry:focus:not(:only-child) + entry,
.linked.vertical > entry:focus:not(:only-child) + button,
.linked.vertical > entry:focus:not(:only-child) + combobox > box > button.combo {
  border-top-color: #13161d; }

.linked.vertical > entry + entry:drop(active):not(:last-child),
.linked.vertical > entry + entry:drop(active):last-child {
  border-top-color: #13161d; }

.linked.vertical > entry:drop(active):not(:only-child) + entry,
.linked.vertical > entry:drop(active):not(:only-child) + button,
.linked.vertical > entry:drop(active):not(:only-child) + combobox > box > button.combo {
  border-top-color: #13161d; }

.linked.vertical > entry + entry.warning:focus:not(:last-child),
.linked.vertical > entry + entry.warning:focus:last-child {
  border-top-color: #13161d; }

.linked.vertical > entry.warning:focus:not(:only-child) + entry,
.linked.vertical > entry.warning:focus:not(:only-child) + button,
.linked.vertical > entry.warning:focus:not(:only-child) + combobox > box > button.combo {
  border-top-color: #13161d; }

.linked.vertical > entry + entry.error:focus:not(:last-child),
.linked.vertical > entry + entry.error:focus:last-child {
  border-top-color: #13161d; }

.linked.vertical > entry.error:focus:not(:only-child) + entry,
.linked.vertical > entry.error:focus:not(:only-child) + button,
.linked.vertical > entry.error:focus:not(:only-child) + combobox > box > button.combo {
  border-top-color: #13161d; }

.linked.vertical > button:active + entry,
.linked.vertical > button:checked + entry {
  border-top-color: #13161d; }

.linked.vertical > button + button {
  border-top-style: none; }

.linked.vertical > button:not(:checked):not(:active):not(.suggested-action):not(.destructive-action):hover:not(:only-child),
.linked.vertical > button:not(:checked):not(:active):not(.suggested-action):not(.destructive-action):hover + button:not(:checked):not(:active):not(.suggested-action):not(.destructive-action) {
  box-shadow: inset 0 1px #13161d; }

.linked.vertical > button:not(:checked):not(:active):not(.suggested-action):not(.destructive-action):disabled:not(:only-child),
.linked.vertical > button:not(:checked):not(:active):not(.suggested-action):not(.destructive-action):disabled + button:not(:checked):not(:active):not(.suggested-action):not(.destructive-action):not(:hover) {
  box-shadow: inset 0 1px rgba(19, 22, 29, 0.5); }

.linked.vertical > button:active + button:not(:checked):not(:active):not(.suggested-action):not(.destructive-action):hover,
.linked.vertical > button:checked + button:not(:checked):not(:active):not(.suggested-action):not(.destructive-action):hover,
.linked.vertical > button.suggested-action + button:not(:checked):not(:active):not(.suggested-action):not(.destructive-action):hover,
.linked.vertical > button.destructive-action + button:not(:checked):not(:active):not(.suggested-action):not(.destructive-action):hover,
.linked.vertical > entry + button:not(:checked):not(:active):not(.suggested-action):not(.destructive-action):hover:not(:only-child),
.linked.vertical > button:not(:checked):not(:active):not(.suggested-action):not(.destructive-action):first-child:disabled,
.linked.vertical > button:not(:checked):not(:active):not(.suggested-action):not(.destructive-action):disabled + button:not(:checked):not(:active):not(.suggested-action):not(.destructive-action):disabled,
.linked.vertical > button:not(:checked):not(:active):not(.suggested-action):not(.destructive-action):first-child:hover,
.linked.vertical > button:active + button:not(:checked):not(:active):not(.suggested-action):not(.destructive-action):disabled,
.linked.vertical > button:checked + button:not(:checked):not(:active):not(.suggested-action):not(.destructive-action):disabled,
.linked.vertical > button.suggested-action + button:not(:checked):not(:active):not(.suggested-action):not(.destructive-action):disabled,
.linked.vertical > button.destructive-action + button:not(:checked):not(:active):not(.suggested-action):not(.destructive-action):disabled,
.linked.vertical > entry + button:not(:checked):not(:active):not(.suggested-action):not(.destructive-action):disabled:not(:only-child) {
  box-shadow: none; }

toolbar.inline-toolbar toolbutton > button.flat, .inline-toolbar toolbutton > button.flat, toolbar.inline-toolbar toolbutton > button.sidebar-button, .inline-toolbar toolbutton > button.sidebar-button, .linked:not(.vertical) > entry,
.linked:not(.vertical) > entry:focus, .inline-toolbar button, .inline-toolbar button:backdrop, .linked:not(.vertical) > button,
.linked:not(.vertical) > button:hover,
.linked:not(.vertical) > button:active,
.linked:not(.vertical) > button:checked, spinbutton:not(.vertical) button, spinbutton:not(.vertical) entry, .primary-toolbar .linked:not(.vertical):not(.path-bar).stack-switcher > button, headerbar .linked:not(.vertical):not(.path-bar).stack-switcher > button, .primary-toolbar .linked:not(.vertical):not(.path-bar).stack-switcher > button:hover, headerbar .linked:not(.vertical):not(.path-bar).stack-switcher > button:hover, .primary-toolbar .linked:not(.vertical):not(.path-bar).stack-switcher > button:active, headerbar .linked:not(.vertical):not(.path-bar).stack-switcher > button:active, .primary-toolbar .linked:not(.vertical):not(.path-bar).stack-switcher > button:checked, headerbar .linked:not(.vertical):not(.path-bar).stack-switcher > button:checked, .primary-toolbar .linked:not(.vertical):not(.path-bar).stack-switcher > button:disabled, headerbar .linked:not(.vertical):not(.path-bar).stack-switcher > button:disabled, .primary-toolbar .linked:not(.vertical).path-bar > button, headerbar .linked:not(.vertical).path-bar > button, .primary-toolbar .linked:not(.vertical).path-bar > button:hover, headerbar .linked:not(.vertical).path-bar > button:hover, .primary-toolbar .linked:not(.vertical).path-bar > button:active, headerbar .linked:not(.vertical).path-bar > button:active, .primary-toolbar .linked:not(.vertical).path-bar > button:checked, headerbar .linked:not(.vertical).path-bar > button:checked, .primary-toolbar .linked:not(.vertical).path-bar > button:disabled, headerbar .linked:not(.vertical).path-bar > button:disabled, .nemo-window .primary-toolbar widget.raised.linked:not(.vertical):not(.path-bar) > button, .nemo-window .primary-toolbar widget.raised.linked:not(.vertical):not(.path-bar) > button:hover, .nemo-window .primary-toolbar widget.raised.linked:not(.vertical):not(.path-bar) > button:active, .nemo-window .primary-toolbar widget.raised.linked:not(.vertical):not(.path-bar) > button:checked, .nemo-window .primary-toolbar widget.raised.linked:not(.vertical):not(.path-bar) > button:disabled, .linked:not(.vertical) > combobox > box > button.combo:dir(ltr), .linked:not(.vertical) > combobox > box > button.combo:dir(rtl) {
  border-radius: 0;
  border-right-style: none; }

.linked:not(.vertical) > entry:first-child, .inline-toolbar button:first-child, .linked:not(.vertical) > button:first-child, toolbar.inline-toolbar toolbutton:first-child > button.flat, .inline-toolbar toolbutton:first-child > button.flat, toolbar.inline-toolbar toolbutton:first-child > button.sidebar-button, .inline-toolbar toolbutton:first-child > button.sidebar-button, spinbutton:not(.vertical) button:first-child, spinbutton:not(.vertical) entry:first-child, .linked:not(.vertical) > combobox:first-child > box > button.combo, .primary-toolbar .linked:not(.vertical):not(.path-bar).stack-switcher > button:first-child, headerbar .linked:not(.vertical):not(.path-bar).stack-switcher > button:first-child, .primary-toolbar .linked:not(.vertical).path-bar > button:first-child, headerbar .linked:not(.vertical).path-bar > button:first-child, .nemo-window .primary-toolbar widget.raised.linked:not(.vertical):not(.path-bar) > button:first-child {
  border-top-left-radius: 3px;
  border-bottom-left-radius: 3px; }

.linked:not(.vertical) > entry:last-child, .inline-toolbar button:last-child, .linked:not(.vertical) > button:last-child, toolbar.inline-toolbar toolbutton:last-child > button.flat, .inline-toolbar toolbutton:last-child > button.flat, toolbar.inline-toolbar toolbutton:last-child > button.sidebar-button, .inline-toolbar toolbutton:last-child > button.sidebar-button, spinbutton:not(.vertical) button:last-child, spinbutton:not(.vertical) entry:last-child, .linked:not(.vertical) > combobox:last-child > box > button.combo, .primary-toolbar .linked:not(.vertical):not(.path-bar).stack-switcher > button:last-child, headerbar .linked:not(.vertical):not(.path-bar).stack-switcher > button:last-child, .primary-toolbar .linked:not(.vertical).path-bar > button:last-child, headerbar .linked:not(.vertical).path-bar > button:last-child, .nemo-window .primary-toolbar widget.raised.linked:not(.vertical):not(.path-bar) > button:last-child {
  border-top-right-radius: 3px;
  border-bottom-right-radius: 3px;
  border-right-style: solid; }

.linked:not(.vertical) > entry:only-child, .inline-toolbar button:only-child, .linked:not(.vertical) > button:only-child, toolbar.inline-toolbar toolbutton:only-child > button.flat, .inline-toolbar toolbutton:only-child > button.flat, toolbar.inline-toolbar toolbutton:only-child > button.sidebar-button, .inline-toolbar toolbutton:only-child > button.sidebar-button, spinbutton:not(.vertical) button:only-child, spinbutton:not(.vertical) entry:only-child, .linked:not(.vertical) > combobox:only-child > box > button.combo, .primary-toolbar .linked:not(.vertical):not(.path-bar).stack-switcher > button:only-child, headerbar .linked:not(.vertical):not(.path-bar).stack-switcher > button:only-child, .primary-toolbar .linked:not(.vertical).path-bar > button:only-child, headerbar .linked:not(.vertical).path-bar > button:only-child, .nemo-window .primary-toolbar widget.raised.linked:not(.vertical):not(.path-bar) > button:only-child {
  border-radius: 3px;
  border-style: solid; }

.linked.vertical > entry,
.linked.vertical > entry:focus, .linked.vertical > button,
.linked.vertical > button:hover,
.linked.vertical > button:active,
.linked.vertical > button:checked, spinbutton.vertical button, spinbutton.vertical entry, .linked.vertical > combobox > box > button.combo {
  border-radius: 0;
  border-bottom-style: none; }

.linked.vertical > entry:first-child, .linked.vertical > button:first-child, spinbutton.vertical button:first-child, spinbutton.vertical entry:first-child, .linked.vertical > combobox:first-child > box > button.combo {
  border-top-left-radius: 3px;
  border-top-right-radius: 3px; }

.linked.vertical > entry:last-child, .linked.vertical > button:last-child, spinbutton.vertical button:last-child, spinbutton.vertical entry:last-child, .linked.vertical > combobox:last-child > box > button.combo {
  border-bottom-left-radius: 3px;
  border-bottom-right-radius: 3px;
  border-bottom-style: solid; }

.linked.vertical > entry:only-child, .linked.vertical > button:only-child, spinbutton.vertical button:only-child, spinbutton.vertical entry:only-child, .linked.vertical > combobox:only-child > box > button.combo {
  border-radius: 3px;
  border-style: solid; }

menuitem.button.flat,
modelbutton.flat, button:link, button:visited, button:link:hover, button:link:active, button:link:checked, button:visited:hover, button:visited:active, button:visited:checked, notebook > header > tabs > tab button.flat:hover, notebook > header > tabs > tab button.sidebar-button:hover, notebook > header > tabs > tab button.flat:active, notebook > header > tabs > tab button.sidebar-button:active, notebook > header > tabs > tab button.flat:active:hover, notebook > header > tabs > tab button.sidebar-button:active:hover, .app-notification button.flat, .app-notification button.sidebar-button, .app-notification button.flat:disabled, .app-notification button.sidebar-button:disabled, calendar.button {
  border-color: transparent;
  background-color: transparent;
  background-image: none;
  box-shadow: none; }

menuitem.button.flat,
modelbutton.flat {
  transition: none;
  min-height: 24px;
  padding-left: 8px;
  padding-right: 8px;
  outline-offset: -3px;
  border-radius: 2px; }
  menuitem.button.flat:hover,
  modelbutton.flat:hover {
    background-color: #30353f; }
  menuitem.button.flat:checked,
  modelbutton.flat:checked {
    color: """
            + color1
            + """; }
  menuitem.button.flat check:last-child,
  menuitem.button.flat radio:last-child,
  modelbutton.flat check:last-child,
  modelbutton.flat radio:last-child {
    margin-left: 8px; }
  menuitem.button.flat check:first-child,
  menuitem.button.flat radio:first-child,
  modelbutton.flat check:first-child,
  modelbutton.flat radio:first-child {
    margin-right: 8px; }

modelbutton.flat arrow.left {
  -gtk-icon-source: -gtk-icontheme("pan-start-symbolic"); }

modelbutton.flat arrow.right {
  -gtk-icon-source: -gtk-icontheme("pan-end-symbolic"); }

*:link, button:link, button:visited {
  color: #59779b; }
  *:link:visited, button:visited {
    color: #475e7a; }
    *:selected *:link:visited, *:selected button:visited:link, *:selected button:visited {
      color: #8f969b; }
  *:link:hover, button:hover:link, button:hover:visited {
    color: #7790b0; }
    *:selected *:link:hover, *:selected button:hover:link, *:selected button:hover:visited {
      color: #bcbfbb; }
  *:link:active, button:active:link, button:active:visited {
    color: #59779b; }
    *:selected *:link:active, *:selected button:active:link, *:selected button:active:visited {
      color: #adb1b0; }
  infobar.info *:link, infobar.info button:link, infobar.info button:visited, infobar.question *:link, infobar.question button:link, infobar.question button:visited, infobar.warning *:link, infobar.warning button:link, infobar.warning button:visited, infobar.error *:link, infobar.error button:link, infobar.error button:visited, *:link:selected, button:selected:link, button:selected:visited, headerbar.selection-mode .subtitle:link, .selection-mode.titlebar:not(headerbar) .subtitle:link,
  *:selected *:link,
  *:selected button:link,
  *:selected button:visited {
    color: #adb1b0; }

button:link > label, button:visited > label {
  text-decoration-line: underline; }

spinbutton:drop(active) {
  box-shadow: none; }

spinbutton button:active {
  color: """
            + color1
            + """; }

spinbutton:disabled {
  color: rgba(203, 204, 198, 0.45); }

spinbutton:not(.vertical) entry {
  min-width: 28px; }

spinbutton:not(.vertical):dir(ltr) entry,
spinbutton:not(.vertical):dir(rtl) button.up {
  border-radius: 3px 0 0 3px; }

spinbutton:not(.vertical) > button + button {
  border-left-style: none; }

spinbutton:not(.vertical) > button:hover:not(:active),
spinbutton:not(.vertical) > button:hover + button {
  box-shadow: inset 1px 0 #13161d; }

spinbutton:not(.vertical) > button:disabled + button:not(:disabled):not(:active):not(:checked):not(:hover),
spinbutton:not(.vertical) > button:not(:disabled):not(:active):not(:checked):not(:hover) + button:disabled {
  box-shadow: inset 1px 0 rgba(19, 22, 29, 0.5); }

spinbutton:not(.vertical) > button:first-child:hover:not(:active),
spinbutton:not(.vertical) > button.up:dir(rtl):hover:not(:active),
spinbutton:not(.vertical) > entry + button:not(:active):hover {
  box-shadow: none; }

spinbutton:not(.vertical) > entry:focus + button {
  border-left-color: #13161d; }

spinbutton:not(.vertical) > entry:drop(active) + button {
  border-left-color: #F08437; }

.osd spinbutton:not(.vertical) > button:hover:not(:active),
.osd spinbutton:not(.vertical) > button:hover + button {
  box-shadow: inset 1px 0 rgba(10, 12, 15, 0.35); }

.osd spinbutton:not(.vertical) > button:first-child:hover:not(:active),
.osd spinbutton:not(.vertical) > button.up:dir(rtl):hover:not(:active),
.osd spinbutton:not(.vertical) > entry + button:not(:active):hover {
  box-shadow: none; }

.osd spinbutton:not(.vertical) > entry:focus + button {
  border-left-color: rgba(10, 12, 15, 0.35); }

spinbutton.vertical button, spinbutton.vertical entry {
  padding-left: 4px;
  padding-right: 4px;
  min-width: 0; }

spinbutton.vertical button.up {
  border-radius: 3px 3px 0 0; }

spinbutton.vertical > entry:focus + button {
  border-top-color: #13161d; }

spinbutton.vertical > entry:drop(active) + button {
  border-top-color: #F08437; }

combobox button.combo {
  min-width: 0;
  padding-left: 8px;
  padding-right: 8px; }

combobox arrow {
  -gtk-icon-source: -gtk-icontheme("pan-down-symbolic");
  min-height: 16px;
  min-width: 16px; }

toolbar, .inline-toolbar {
  -GtkWidget-window-dragging: true;
  padding: 4px;
  background-color: """
            + color6
            + """; }
  toolbar separator, .inline-toolbar separator {
    background: none; }
  toolbar.horizontal separator, .horizontal.inline-toolbar separator {
    margin: 0 6px; }
  toolbar.vertical separator, .vertical.inline-toolbar separator {
    margin: 6px 0; }
  .osd toolbar, .osd .inline-toolbar {
    background-color: transparent; }
  toolbar.osd, .osd.inline-toolbar {
    padding: 7px;
    border: 1px solid rgba(0, 0, 0, 0.5);
    border-radius: 3px;
    background-color: rgba(35, 40, 52, 0.85); }
    toolbar.osd.left, .osd.left.inline-toolbar, toolbar.osd.right, .osd.right.inline-toolbar, toolbar.osd.top, .osd.top.inline-toolbar, toolbar.osd.bottom, .osd.bottom.inline-toolbar {
      border-radius: 0; }
    toolbar.osd.top, .osd.top.inline-toolbar {
      border-width: 0 0 1px 0; }
    toolbar.osd.bottom, .osd.bottom.inline-toolbar {
      border-width: 1px 0 0 0; }
    toolbar.osd.left, .osd.left.inline-toolbar {
      border-width: 0 1px 0 0; }
    toolbar.osd.right, .osd.right.inline-toolbar {
      border-width: 0 0 0 1px; }
  toolbar:not(.inline-toolbar) switch, .inline-toolbar:not(.inline-toolbar) switch,
  toolbar:not(.inline-toolbar) scale, .inline-toolbar:not(.inline-toolbar) scale,
  toolbar:not(.inline-toolbar) entry, .inline-toolbar:not(.inline-toolbar) entry,
  toolbar:not(.inline-toolbar) spinbutton, .inline-toolbar:not(.inline-toolbar) spinbutton,
  toolbar:not(.inline-toolbar) button, .inline-toolbar:not(.inline-toolbar) button {
    margin-right: 1px;
    margin-bottom: 1px; }
  toolbar:not(.inline-toolbar) .linked > button, .inline-toolbar:not(.inline-toolbar) .linked > button,
  toolbar:not(.inline-toolbar) .linked > entry, .inline-toolbar:not(.inline-toolbar) .linked > entry {
    margin-right: 0; }

.primary-toolbar:not(.libreoffice-toolbar) {
  color: rgba(207, 209, 193, 0.8);
  background-color: """
            + color6
            + """;
  box-shadow: none;
  border-width: 0 0 1px 0;
  border-style: solid;
  border-image: linear-gradient(to bottom, """
            + color6
            + """, rgba(17, 20, 26, 0.97)) 1 0 1 0; }

.inline-toolbar {
  background-color: """
            + color6
            + """;
  border-style: solid;
  border-color: #13161d;
  border-width: 0 1px 1px;
  padding: 3px;
  border-radius: 0  0 3px 3px; }

searchbar {
  background-color: """
            + color6
            + """;
  border-style: solid;
  border-color: #13161d;
  border-width: 0 0 1px;
  padding: 3px; }

actionbar {
  padding: 6px;
  border-top: 1px solid #13161d;
  background-color: """
            + color6
            + """; }

headerbar,
.titlebar:not(headerbar) {
  min-height: 42px;
  padding: 0 7px;
  border-width: 0 0 1px;
  border-style: solid;
  border-color: #171b24;
  color: rgba(207, 209, 193, 0.8);
  background-color: """
            + color6
            + """;
  box-shadow: inset 0 1px rgba(37, 43, 57, 0.97); }
  .csd headerbar,
  .csd .titlebar:not(headerbar) {
    background-color: rgba(31, 36, 48, 0.97);
    border-color: rgba(23, 27, 36, 0.97); }
  headerbar:backdrop,
  .titlebar:backdrop:not(headerbar) {
    transition: 200ms ease-out;
    color: rgba(207, 209, 193, 0.5);
    background-color: #222735; }
    .csd headerbar:backdrop,
    .csd .titlebar:backdrop:not(headerbar) {
      background-color: rgba(34, 39, 53, 0.97); }
  headerbar .title, .titlebar:not(headerbar) .title {
    padding-left: 12px;
    padding-right: 12px; }
  headerbar .subtitle, .titlebar:not(headerbar) .subtitle {
    font-size: smaller;
    padding-left: 12px;
    padding-right: 12px; }
  headerbar.selection-mode,
  .selection-mode.titlebar:not(headerbar) {
    color: """
            + color1
            + """;
    background-color: rgba(52, 69, 90, 0.95);
    border-color: rgba(45, 59, 77, 0.95);
    box-shadow: none; }
    headerbar.selection-mode:backdrop,
    .selection-mode.titlebar:backdrop:not(headerbar) {
      background-color: rgba(52, 69, 90, 0.95);
      color: rgba(203, 204, 198, 0.6); }
    headerbar.selection-mode .selection-menu, .selection-mode.titlebar:not(headerbar) .selection-menu {
      box-shadow: none;
      padding-left: 10px;
      padding-right: 10px; }
      headerbar.selection-mode .selection-menu GtkArrow, .selection-mode.titlebar:not(headerbar) .selection-menu GtkArrow {
        -GtkArrow-arrow-scaling: 1; }
      headerbar.selection-mode .selection-menu .arrow, .selection-mode.titlebar:not(headerbar) .selection-menu .arrow {
        -gtk-icon-source: -gtk-icontheme("pan-down-symbolic"); }
    .maximized headerbar.selection-mode,
    .maximized .selection-mode.titlebar:not(headerbar) {
      background-color: #34455a; }
  .tiled headerbar, .tiled headerbar:backdrop,
  .maximized headerbar, .maximized headerbar:backdrop,
  .tiled .titlebar:not(headerbar),
  .tiled .titlebar:backdrop:not(headerbar),
  .maximized .titlebar:not(headerbar),
  .maximized .titlebar:backdrop:not(headerbar) {
    border-radius: 0; }
  .maximized headerbar,
  .maximized .titlebar:not(headerbar) {
    background-color: """
            + color6
            + """;
    border-color: #171b24; }
    .maximized headerbar:backdrop,
    .maximized .titlebar:backdrop:not(headerbar) {
      background-color: #222735; }
  headerbar.default-decoration,
  .csd headerbar.default-decoration, headerbar.default-decoration:backdrop,
  .csd headerbar.default-decoration:backdrop,
  .default-decoration.titlebar:not(headerbar),
  .csd .default-decoration.titlebar:not(headerbar),
  .default-decoration.titlebar:backdrop:not(headerbar),
  .csd .default-decoration.titlebar:backdrop:not(headerbar) {
    min-height: 28px;
    padding: 0 3px;
    background-color: """
            + color6
            + """;
    border-bottom-width: 0; }
    .maximized headerbar.default-decoration, .maximized
    .csd headerbar.default-decoration, .maximized headerbar.default-decoration:backdrop, .maximized
    .csd headerbar.default-decoration:backdrop,
    .maximized .default-decoration.titlebar:not(headerbar),
    .maximized
    .csd .default-decoration.titlebar:not(headerbar),
    .maximized .default-decoration.titlebar:backdrop:not(headerbar),
    .maximized
    .csd .default-decoration.titlebar:backdrop:not(headerbar) {
      background-color: """
            + color6
            + """; }

.titlebar {
  border-radius: 3px 3px 0 0; }

headerbar entry, headerbar button, headerbar separator {
  margin-top: 6px;
  margin-bottom: 6px; }

separator:first-child + headerbar, separator:first-child + headerbar:backdrop, headerbar:first-child, headerbar:first-child:backdrop {
  border-top-left-radius: 3px; }
  .maximized separator:first-child + headerbar,
  .tiled separator:first-child + headerbar, .maximized separator:first-child + headerbar:backdrop,
  .tiled separator:first-child + headerbar:backdrop, .maximized headerbar:first-child,
  .tiled headerbar:first-child, .maximized headerbar:first-child:backdrop,
  .tiled headerbar:first-child:backdrop {
    border-radius: 0; }

headerbar:last-child, headerbar:last-child:backdrop {
  border-top-right-radius: 3px; }
  .maximized headerbar:last-child,
  .tiled headerbar:last-child, .maximized headerbar:last-child:backdrop,
  .tiled headerbar:last-child:backdrop {
    border-radius: 0; }

window > .titlebar:not(headerbar), window > .titlebar:not(headerbar):backdrop,
window.csd > .titlebar:not(headerbar),
window.csd > .titlebar:not(headerbar):backdrop {
  padding: 0;
  background: none;
  border: none;
  box-shadow: none; }

.titlebar:not(headerbar) > separator {
  background-image: linear-gradient(to bottom, rgba(23, 27, 36, 0.97), rgba(23, 27, 36, 0.97)); }

.primary-toolbar:not(.libreoffice-toolbar) separator, headerbar separator.titlebutton, .titlebar:not(headerbar) separator.titlebutton {
  min-width: 1px;
  min-height: 1px;
  background: none;
  border-width: 0 1px;
  border-image: linear-gradient(to bottom, rgba(207, 209, 193, 0) 25%, rgba(207, 209, 193, 0.15) 25%, rgba(207, 209, 193, 0.15) 75%, rgba(207, 209, 193, 0) 75%) 0 1/0 1px stretch; }
  .primary-toolbar:not(.libreoffice-toolbar) separator:backdrop, headerbar separator.titlebutton:backdrop, .titlebar:not(headerbar) separator.titlebutton:backdrop {
    opacity: 0.6; }

.primary-toolbar entry, headerbar entry {
  color: rgba(207, 209, 193, 0.8);
  border-color: rgba(7, 8, 11, 0.37);
  background-color: rgba(75, 87, 116, 0.37); }
  .primary-toolbar entry image, headerbar entry image, .primary-toolbar entry image:hover, headerbar entry image:hover {
    color: inherit; }
  .primary-toolbar entry:backdrop, headerbar entry:backdrop {
    opacity: 0.85; }
  .primary-toolbar entry:focus, headerbar entry:focus {
    color: """
            + color1
            + """;
    border-color: transparent;
    background-color: """
            + color4
            + """;
    background-clip: padding-box; }
    .primary-toolbar entry:focus image, headerbar entry:focus image {
      color: """
            + color1
            + """; }
  .primary-toolbar entry:disabled, headerbar entry:disabled {
    color: rgba(207, 209, 193, 0.35);
    border-color: rgba(7, 8, 11, 0.37);
    background-color: rgba(75, 87, 116, 0.22); }
  .primary-toolbar entry selection:focus, headerbar entry selection:focus {
    background-color: """
            + color1
            + """;
    color: """
            + color4
            + """; }
  .primary-toolbar entry progress, headerbar entry progress {
    border-color: """
            + color4
            + """;
    background-image: none;
    background-color: transparent; }
  .primary-toolbar entry.warning, headerbar entry.warning {
    color: white;
    border-color: rgba(7, 8, 11, 0.37);
    background-color: rgba(161, 88, 51, 0.988); }
    .primary-toolbar entry.warning:focus, headerbar entry.warning:focus {
      color: white;
      background-color: #F27835; }
    .primary-toolbar entry.warning selection, headerbar entry.warning selection, .primary-toolbar entry.warning selection:focus, headerbar entry.warning selection:focus {
      background-color: white;
      color: #F27835; }
  .primary-toolbar entry.error, headerbar entry.error {
    color: white;
    border-color: rgba(7, 8, 11, 0.37);
    background-color: rgba(167, 54, 53, 0.988); }
    .primary-toolbar entry.error:focus, headerbar entry.error:focus {
      color: white;
      background-color: #FC4138; }
    .primary-toolbar entry.error selection, headerbar entry.error selection, .primary-toolbar entry.error selection:focus, headerbar entry.error selection:focus {
      background-color: white;
      color: #FC4138; }

.primary-toolbar button, headerbar button {
  color: rgba(207, 209, 193, 0.8);
  outline-offset: -3px;
  background-color: rgba(31, 36, 48, 0);
  border-color: rgba(31, 36, 48, 0); }
  .primary-toolbar button:backdrop, headerbar button:backdrop {
    opacity: 0.7; }
  .primary-toolbar button:hover, headerbar button:hover {
    color: rgba(207, 209, 193, 0.8);
    border-color: rgba(7, 8, 11, 0.37);
    background-color: rgba(75, 87, 116, 0.37); }
  .primary-toolbar button:active, headerbar button:active, .primary-toolbar button:checked, headerbar button:checked {
    color: """
            + color1
            + """;
    border-color: transparent;
    background-color: """
            + color4
            + """;
    background-clip: padding-box; }
  .primary-toolbar button:disabled, headerbar button:disabled {
    background-color: rgba(31, 36, 48, 0);
    border-color: rgba(31, 36, 48, 0); }
    .primary-toolbar button:disabled label, headerbar button:disabled label, .primary-toolbar button:disabled, headerbar button:disabled {
      color: rgba(207, 209, 193, 0.35); }
  .primary-toolbar button:disabled:active, headerbar button:disabled:active, .primary-toolbar button:disabled:checked, headerbar button:disabled:checked {
    color: rgba(203, 204, 198, 0.75);
    border-color: rgba(52, 69, 90, 0.65);
    background-color: rgba(52, 69, 90, 0.65); }

.selection-mode.primary-toolbar button, headerbar.selection-mode button, .selection-mode.primary-toolbar button.flat, headerbar.selection-mode button.flat, .selection-mode.primary-toolbar button.sidebar-button, headerbar.selection-mode button.sidebar-button {
  border-color: transparent;
  background-color: transparent;
  background-image: none;
  color: """
            + color1
            + """;
  background-color: rgba(203, 204, 198, 0); }

.primary-toolbar .linked:not(.vertical):not(.path-bar):not(.stack-switcher) button:not(:last-child):not(:only-child), headerbar .linked:not(.vertical):not(.path-bar):not(.stack-switcher) button:not(:last-child):not(:only-child) {
  margin-right: 1px; }

.primary-toolbar .linked:not(.vertical):not(.path-bar) > button, headerbar .linked:not(.vertical):not(.path-bar) > button, .primary-toolbar .linked:not(.vertical):not(.path-bar) > button:hover, headerbar .linked:not(.vertical):not(.path-bar) > button:hover, .primary-toolbar .linked:not(.vertical):not(.path-bar) > button:active, headerbar .linked:not(.vertical):not(.path-bar) > button:active, .primary-toolbar .linked:not(.vertical):not(.path-bar) > button:checked, headerbar .linked:not(.vertical):not(.path-bar) > button:checked, .primary-toolbar .linked:not(.vertical):not(.path-bar) > button:disabled, headerbar .linked:not(.vertical):not(.path-bar) > button:disabled {
  border-radius: 3px;
  border-style: solid; }

.primary-toolbar .linked:not(.vertical):not(.path-bar) > button:not(:checked):not(:active):not(.suggested-action):not(.destructive-action):hover:not(:only-child), headerbar .linked:not(.vertical):not(.path-bar) > button:not(:checked):not(:active):not(.suggested-action):not(.destructive-action):hover:not(:only-child), .primary-toolbar .linked:not(.vertical):not(.path-bar) > button:not(:checked):not(:active):not(.suggested-action):not(.destructive-action):hover + button:not(:checked):not(:active):not(.suggested-action):not(.destructive-action), headerbar .linked:not(.vertical):not(.path-bar) > button:not(:checked):not(:active):not(.suggested-action):not(.destructive-action):hover + button:not(:checked):not(:active):not(.suggested-action):not(.destructive-action), .primary-toolbar .linked:not(.vertical):not(.path-bar) > button:not(:checked):not(:active):not(.suggested-action):not(.destructive-action):disabled:not(:only-child), headerbar .linked:not(.vertical):not(.path-bar) > button:not(:checked):not(:active):not(.suggested-action):not(.destructive-action):disabled:not(:only-child), .primary-toolbar .linked:not(.vertical):not(.path-bar) > button:not(:checked):not(:active):not(.suggested-action):not(.destructive-action):disabled + button:not(:checked):not(:active):not(.suggested-action):not(.destructive-action):not(:hover), headerbar .linked:not(.vertical):not(.path-bar) > button:not(:checked):not(:active):not(.suggested-action):not(.destructive-action):disabled + button:not(:checked):not(:active):not(.suggested-action):not(.destructive-action):not(:hover) {
  box-shadow: none; }

.primary-toolbar .linked:not(.vertical):not(.path-bar).stack-switcher > button, headerbar .linked:not(.vertical):not(.path-bar).stack-switcher > button, .primary-toolbar .linked:not(.vertical).path-bar > button, headerbar .linked:not(.vertical).path-bar > button {
  color: rgba(207, 209, 193, 0.8);
  border-color: rgba(7, 8, 11, 0.37);
  background-color: rgba(75, 87, 116, 0.37); }
  .primary-toolbar .linked:not(.vertical):not(.path-bar).stack-switcher > button:hover, headerbar .linked:not(.vertical):not(.path-bar).stack-switcher > button:hover, .primary-toolbar .linked:not(.vertical).path-bar > button:hover, headerbar .linked:not(.vertical).path-bar > button:hover {
    background-color: rgba(108, 123, 160, 0.37); }
  .primary-toolbar .linked:not(.vertical):not(.path-bar).stack-switcher > button:active, headerbar .linked:not(.vertical):not(.path-bar).stack-switcher > button:active, .primary-toolbar .linked:not(.vertical):not(.path-bar).stack-switcher > button:checked, headerbar .linked:not(.vertical):not(.path-bar).stack-switcher > button:checked, .primary-toolbar .linked:not(.vertical).path-bar > button:active, headerbar .linked:not(.vertical).path-bar > button:active, .primary-toolbar .linked:not(.vertical).path-bar > button:checked, headerbar .linked:not(.vertical).path-bar > button:checked {
    color: """
            + color1
            + """;
    border-color: transparent;
    background-color: """
            + color4
            + """; }
  .primary-toolbar .linked:not(.vertical):not(.path-bar).stack-switcher > button:disabled, headerbar .linked:not(.vertical):not(.path-bar).stack-switcher > button:disabled, .primary-toolbar .linked:not(.vertical).path-bar > button:disabled, headerbar .linked:not(.vertical).path-bar > button:disabled {
    color: rgba(207, 209, 193, 0.4); }

.primary-toolbar .linked:not(.vertical):not(.path-bar).stack-switcher > button + button, headerbar .linked:not(.vertical):not(.path-bar).stack-switcher > button + button, .primary-toolbar .linked:not(.vertical).path-bar > button + button, headerbar .linked:not(.vertical).path-bar > button + button {
  border-left-style: none; }

.primary-toolbar .linked:not(.vertical):not(.path-bar).stack-switcher > button:hover:not(:checked):not(:active):not(:only-child):hover, headerbar .linked:not(.vertical):not(.path-bar).stack-switcher > button:hover:not(:checked):not(:active):not(:only-child):hover, .primary-toolbar .linked:not(.vertical).path-bar > button:hover:not(:checked):not(:active):not(:only-child):hover, headerbar .linked:not(.vertical).path-bar > button:hover:not(:checked):not(:active):not(:only-child):hover {
  box-shadow: inset 1px 0 rgba(7, 8, 11, 0.37), inset -1px 0 rgba(7, 8, 11, 0.37); }

.primary-toolbar .linked:not(.vertical):not(.path-bar).stack-switcher > button:hover:not(:checked):not(:active):not(:only-child):first-child:hover, headerbar .linked:not(.vertical):not(.path-bar).stack-switcher > button:hover:not(:checked):not(:active):not(:only-child):first-child:hover, .primary-toolbar .linked:not(.vertical).path-bar > button:hover:not(:checked):not(:active):not(:only-child):first-child:hover, headerbar .linked:not(.vertical).path-bar > button:hover:not(:checked):not(:active):not(:only-child):first-child:hover {
  box-shadow: inset -1px 0 rgba(7, 8, 11, 0.37); }

.primary-toolbar .linked:not(.vertical):not(.path-bar).stack-switcher > button:hover:not(:checked):not(:active):not(:only-child):last-child:hover, headerbar .linked:not(.vertical):not(.path-bar).stack-switcher > button:hover:not(:checked):not(:active):not(:only-child):last-child:hover, .primary-toolbar .linked:not(.vertical).path-bar > button:hover:not(:checked):not(:active):not(:only-child):last-child:hover, headerbar .linked:not(.vertical).path-bar > button:hover:not(:checked):not(:active):not(:only-child):last-child:hover {
  box-shadow: inset 1px 0 rgba(7, 8, 11, 0.37); }

.primary-toolbar .linked:not(.vertical):not(.path-bar) > entry + entry, headerbar .linked:not(.vertical):not(.path-bar) > entry + entry {
  border-left-color: rgba(7, 8, 11, 0); }

.primary-toolbar .linked:not(.vertical):not(.path-bar) > entry.error + entry, headerbar .linked:not(.vertical):not(.path-bar) > entry.error + entry, .primary-toolbar .linked:not(.vertical):not(.path-bar) > entry + entry.error, headerbar .linked:not(.vertical):not(.path-bar) > entry + entry.error {
  border-left-color: rgba(7, 8, 11, 0); }

.primary-toolbar .linked:not(.vertical):not(.path-bar) > entry.warning + entry, headerbar .linked:not(.vertical):not(.path-bar) > entry.warning + entry, .primary-toolbar .linked:not(.vertical):not(.path-bar) > entry + entry.warning, headerbar .linked:not(.vertical):not(.path-bar) > entry + entry.warning {
  border-left-color: rgba(7, 8, 11, 0); }

.primary-toolbar .linked:not(.vertical):not(.path-bar) > entry.error + entry.warning, headerbar .linked:not(.vertical):not(.path-bar) > entry.error + entry.warning, .primary-toolbar .linked:not(.vertical):not(.path-bar) > entry.warning + entry.error, headerbar .linked:not(.vertical):not(.path-bar) > entry.warning + entry.error {
  border-left-color: rgba(7, 8, 11, 0); }

.primary-toolbar .linked:not(.vertical):not(.path-bar) > entry + entry:focus:not(:last-child), headerbar .linked:not(.vertical):not(.path-bar) > entry + entry:focus:not(:last-child), .primary-toolbar .linked:not(.vertical):not(.path-bar) > entry + entry:focus:last-child, headerbar .linked:not(.vertical):not(.path-bar) > entry + entry:focus:last-child {
  border-left-color: rgba(7, 8, 11, 0.37); }

.primary-toolbar .linked:not(.vertical):not(.path-bar) > entry:focus:not(:only-child) + entry, headerbar .linked:not(.vertical):not(.path-bar) > entry:focus:not(:only-child) + entry, .primary-toolbar .linked:not(.vertical):not(.path-bar) > entry:focus:not(:only-child) + button, headerbar .linked:not(.vertical):not(.path-bar) > entry:focus:not(:only-child) + button, .primary-toolbar .linked:not(.vertical):not(.path-bar) > entry:focus:not(:only-child) + combobox > box > button.combo, headerbar .linked:not(.vertical):not(.path-bar) > entry:focus:not(:only-child) + combobox > box > button.combo {
  border-left-color: rgba(7, 8, 11, 0.37); }

.primary-toolbar .linked:not(.vertical):not(.path-bar) > entry + entry:drop(active):not(:last-child), headerbar .linked:not(.vertical):not(.path-bar) > entry + entry:drop(active):not(:last-child), .primary-toolbar .linked:not(.vertical):not(.path-bar) > entry + entry:drop(active):last-child, headerbar .linked:not(.vertical):not(.path-bar) > entry + entry:drop(active):last-child {
  border-left-color: rgba(7, 8, 11, 0.37); }

.primary-toolbar .linked:not(.vertical):not(.path-bar) > entry:drop(active):not(:only-child) + entry, headerbar .linked:not(.vertical):not(.path-bar) > entry:drop(active):not(:only-child) + entry, .primary-toolbar .linked:not(.vertical):not(.path-bar) > entry:drop(active):not(:only-child) + button, headerbar .linked:not(.vertical):not(.path-bar) > entry:drop(active):not(:only-child) + button, .primary-toolbar .linked:not(.vertical):not(.path-bar) > entry:drop(active):not(:only-child) + combobox > box > button.combo, headerbar .linked:not(.vertical):not(.path-bar) > entry:drop(active):not(:only-child) + combobox > box > button.combo {
  border-left-color: rgba(7, 8, 11, 0.37); }

.primary-toolbar .linked:not(.vertical):not(.path-bar) > entry + entry.warning:focus:not(:last-child), headerbar .linked:not(.vertical):not(.path-bar) > entry + entry.warning:focus:not(:last-child), .primary-toolbar .linked:not(.vertical):not(.path-bar) > entry + entry.warning:focus:last-child, headerbar .linked:not(.vertical):not(.path-bar) > entry + entry.warning:focus:last-child {
  border-left-color: rgba(7, 8, 11, 0.37); }

.primary-toolbar .linked:not(.vertical):not(.path-bar) > entry.warning:focus:not(:only-child) + entry, headerbar .linked:not(.vertical):not(.path-bar) > entry.warning:focus:not(:only-child) + entry, .primary-toolbar .linked:not(.vertical):not(.path-bar) > entry.warning:focus:not(:only-child) + button, headerbar .linked:not(.vertical):not(.path-bar) > entry.warning:focus:not(:only-child) + button, .primary-toolbar .linked:not(.vertical):not(.path-bar) > entry.warning:focus:not(:only-child) + combobox > box > button.combo, headerbar .linked:not(.vertical):not(.path-bar) > entry.warning:focus:not(:only-child) + combobox > box > button.combo {
  border-left-color: rgba(7, 8, 11, 0.37); }

.primary-toolbar .linked:not(.vertical):not(.path-bar) > entry + entry.error:focus:not(:last-child), headerbar .linked:not(.vertical):not(.path-bar) > entry + entry.error:focus:not(:last-child), .primary-toolbar .linked:not(.vertical):not(.path-bar) > entry + entry.error:focus:last-child, headerbar .linked:not(.vertical):not(.path-bar) > entry + entry.error:focus:last-child {
  border-left-color: rgba(7, 8, 11, 0.37); }

.primary-toolbar .linked:not(.vertical):not(.path-bar) > entry.error:focus:not(:only-child) + entry, headerbar .linked:not(.vertical):not(.path-bar) > entry.error:focus:not(:only-child) + entry, .primary-toolbar .linked:not(.vertical):not(.path-bar) > entry.error:focus:not(:only-child) + button, headerbar .linked:not(.vertical):not(.path-bar) > entry.error:focus:not(:only-child) + button, .primary-toolbar .linked:not(.vertical):not(.path-bar) > entry.error:focus:not(:only-child) + combobox > box > button.combo, headerbar .linked:not(.vertical):not(.path-bar) > entry.error:focus:not(:only-child) + combobox > box > button.combo {
  border-left-color: rgba(7, 8, 11, 0.37); }

.primary-toolbar .linked:not(.vertical):not(.path-bar) > button:active + entry, headerbar .linked:not(.vertical):not(.path-bar) > button:active + entry, .primary-toolbar .linked:not(.vertical):not(.path-bar) > button:checked + entry, headerbar .linked:not(.vertical):not(.path-bar) > button:checked + entry {
  border-left-color: rgba(7, 8, 11, 0.37); }

.primary-toolbar button.suggested-action, headerbar button.suggested-action {
  background-clip: border-box;
  color: white;
  background-color: #4DADD4;
  border-color: #4DADD4; }
  .primary-toolbar button.suggested-action.flat, headerbar button.suggested-action.flat, .primary-toolbar button.suggested-action.sidebar-button, headerbar button.suggested-action.sidebar-button {
    border-color: transparent;
    background-color: transparent;
    background-image: none;
    color: #4DADD4; }
  .primary-toolbar button.suggested-action:hover, headerbar button.suggested-action:hover {
    background-clip: border-box;
    color: white;
    background-color: #76c0de;
    border-color: #76c0de; }
  .primary-toolbar button.suggested-action:active, headerbar button.suggested-action:active, .primary-toolbar button.suggested-action:checked, headerbar button.suggested-action:checked {
    background-clip: border-box;
    color: white;
    background-color: #2e96c0;
    border-color: #2e96c0; }
  .primary-toolbar button.suggested-action.flat:disabled, headerbar button.suggested-action.flat:disabled, .primary-toolbar button.suggested-action.sidebar-button:disabled, headerbar button.suggested-action.sidebar-button:disabled, .primary-toolbar button.suggested-action:disabled, headerbar button.suggested-action:disabled {
    background-color: rgba(31, 36, 48, 0);
    border-color: rgba(31, 36, 48, 0); }
    .primary-toolbar button.suggested-action.flat:disabled label, headerbar button.suggested-action.flat:disabled label, .primary-toolbar button.suggested-action.sidebar-button:disabled label, headerbar button.suggested-action.sidebar-button:disabled label, .primary-toolbar button.suggested-action.flat:disabled, headerbar button.suggested-action.flat:disabled, .primary-toolbar button.suggested-action.sidebar-button:disabled, headerbar button.suggested-action.sidebar-button:disabled, .primary-toolbar button.suggested-action:disabled label, headerbar button.suggested-action:disabled label, .primary-toolbar button.suggested-action:disabled, headerbar button.suggested-action:disabled {
      color: rgba(207, 209, 193, 0.35); }

.primary-toolbar button.suggested-action:backdrop, headerbar button.suggested-action:backdrop, .primary-toolbar button.suggested-action:backdrop, headerbar button.suggested-action:backdrop {
  opacity: 0.8; }

.primary-toolbar button.destructive-action, headerbar button.destructive-action {
  background-clip: border-box;
  color: white;
  background-color: #F04A50;
  border-color: #F04A50; }
  .primary-toolbar button.destructive-action.flat, headerbar button.destructive-action.flat, .primary-toolbar button.destructive-action.sidebar-button, headerbar button.destructive-action.sidebar-button {
    border-color: transparent;
    background-color: transparent;
    background-image: none;
    color: #F04A50; }
  .primary-toolbar button.destructive-action:hover, headerbar button.destructive-action:hover {
    background-clip: border-box;
    color: white;
    background-color: #f4797e;
    border-color: #f4797e; }
  .primary-toolbar button.destructive-action:active, headerbar button.destructive-action:active, .primary-toolbar button.destructive-action:checked, headerbar button.destructive-action:checked {
    background-clip: border-box;
    color: white;
    background-color: #ec1b22;
    border-color: #ec1b22; }
  .primary-toolbar button.destructive-action.flat:disabled, headerbar button.destructive-action.flat:disabled, .primary-toolbar button.destructive-action.sidebar-button:disabled, headerbar button.destructive-action.sidebar-button:disabled, .primary-toolbar button.destructive-action:disabled, headerbar button.destructive-action:disabled {
    background-color: rgba(31, 36, 48, 0);
    border-color: rgba(31, 36, 48, 0); }
    .primary-toolbar button.destructive-action.flat:disabled label, headerbar button.destructive-action.flat:disabled label, .primary-toolbar button.destructive-action.sidebar-button:disabled label, headerbar button.destructive-action.sidebar-button:disabled label, .primary-toolbar button.destructive-action.flat:disabled, headerbar button.destructive-action.flat:disabled, .primary-toolbar button.destructive-action.sidebar-button:disabled, headerbar button.destructive-action.sidebar-button:disabled, .primary-toolbar button.destructive-action:disabled label, headerbar button.destructive-action:disabled label, .primary-toolbar button.destructive-action:disabled, headerbar button.destructive-action:disabled {
      color: rgba(207, 209, 193, 0.35); }

.primary-toolbar button.destructive-action:backdrop, headerbar button.destructive-action:backdrop, .primary-toolbar button.destructive-action:backdrop, headerbar button.destructive-action:backdrop {
  opacity: 0.8; }

.primary-toolbar spinbutton:not(.vertical):focus, headerbar spinbutton:not(.vertical):focus {
  color: """
            + color1
            + """;
  caret-color: """
            + color1
            + """; }

.primary-toolbar spinbutton:not(.vertical) button, headerbar spinbutton:not(.vertical) button, .primary-toolbar spinbutton:not(.vertical) button:disabled, headerbar spinbutton:not(.vertical) button:disabled {
  color: rgba(207, 209, 193, 0.8);
  border-color: rgba(7, 8, 11, 0.37);
  background-color: rgba(75, 87, 116, 0.37); }

.primary-toolbar spinbutton:not(.vertical) button:hover, headerbar spinbutton:not(.vertical) button:hover {
  background-color: rgba(108, 123, 160, 0.37); }

.primary-toolbar spinbutton:not(.vertical) button:active, headerbar spinbutton:not(.vertical) button:active, .primary-toolbar spinbutton:not(.vertical) button:checked, headerbar spinbutton:not(.vertical) button:checked {
  color: """
            + color1
            + """;
  border-color: transparent;
  background-color: """
            + color4
            + """; }

.primary-toolbar spinbutton:not(.vertical) button:disabled, headerbar spinbutton:not(.vertical) button:disabled {
  color: rgba(207, 209, 193, 0.4); }

.primary-toolbar spinbutton:not(.vertical) > button + button, headerbar spinbutton:not(.vertical) > button + button {
  border-left-style: none; }

.primary-toolbar spinbutton:not(.vertical) > button:hover:not(:active), headerbar spinbutton:not(.vertical) > button:hover:not(:active), .primary-toolbar spinbutton:not(.vertical) > button:hover + button, headerbar spinbutton:not(.vertical) > button:hover + button {
  box-shadow: inset 1px 0 rgba(7, 8, 11, 0.37); }

.primary-toolbar spinbutton:not(.vertical) > button:disabled + button:not(:disabled):not(:active):not(:checked):not(:hover), headerbar spinbutton:not(.vertical) > button:disabled + button:not(:disabled):not(:active):not(:checked):not(:hover), .primary-toolbar spinbutton:not(.vertical) > button:not(:disabled):not(:active):not(:checked):not(:hover) + button:disabled, headerbar spinbutton:not(.vertical) > button:not(:disabled):not(:active):not(:checked):not(:hover) + button:disabled {
  box-shadow: inset 1px 0 rgba(7, 8, 11, 0.37); }

.primary-toolbar spinbutton:not(.vertical) > button:first-child:hover:not(:active), headerbar spinbutton:not(.vertical) > button:first-child:hover:not(:active), .primary-toolbar spinbutton:not(.vertical) > entry + button:not(:active):hover, headerbar spinbutton:not(.vertical) > entry + button:not(:active):hover {
  box-shadow: none; }

.primary-toolbar spinbutton:not(.vertical) > entry:focus + button, headerbar spinbutton:not(.vertical) > entry:focus + button {
  border-left-color: rgba(7, 8, 11, 0.37); }

.primary-toolbar combobox:disabled, headerbar combobox:disabled {
  color: rgba(207, 209, 193, 0.2); }

.primary-toolbar combobox > .linked > button.combo, headerbar combobox > .linked > button.combo {
  color: rgba(207, 209, 193, 0.8);
  border-color: rgba(7, 8, 11, 0.37);
  background-color: rgba(75, 87, 116, 0.37); }
  .primary-toolbar combobox > .linked > button.combo image, headerbar combobox > .linked > button.combo image, .primary-toolbar combobox > .linked > button.combo image:hover, headerbar combobox > .linked > button.combo image:hover {
    color: inherit; }
  .primary-toolbar combobox > .linked > button.combo:hover, headerbar combobox > .linked > button.combo:hover {
    color: """
            + color1
            + """;
    border-color: transparent;
    background-color: """
            + color4
            + """;
    box-shadow: none; }
  .primary-toolbar combobox > .linked > button.combo:disabled, headerbar combobox > .linked > button.combo:disabled {
    color: rgba(207, 209, 193, 0.35);
    border-color: rgba(7, 8, 11, 0.37);
    background-color: rgba(75, 87, 116, 0.22); }

.primary-toolbar combobox > .linked > entry.combo:dir(ltr), headerbar combobox > .linked > entry.combo:dir(ltr) {
  border-right-style: none; }
  .primary-toolbar combobox > .linked > entry.combo:dir(ltr):focus, headerbar combobox > .linked > entry.combo:dir(ltr):focus {
    box-shadow: none; }

.primary-toolbar combobox > .linked > entry.combo:dir(rtl), headerbar combobox > .linked > entry.combo:dir(rtl) {
  border-left-style: none; }
  .primary-toolbar combobox > .linked > entry.combo:dir(rtl):focus, headerbar combobox > .linked > entry.combo:dir(rtl):focus {
    box-shadow: none; }

.primary-toolbar combobox > .linked > button.combo:dir(ltr), headerbar combobox > .linked > button.combo:dir(ltr), .primary-toolbar combobox > .linked > button.combo:dir(ltr):hover, headerbar combobox > .linked > button.combo:dir(ltr):hover, .primary-toolbar combobox > .linked > button.combo:dir(ltr):active, headerbar combobox > .linked > button.combo:dir(ltr):active, .primary-toolbar combobox > .linked > button.combo:dir(ltr):checked, headerbar combobox > .linked > button.combo:dir(ltr):checked, .primary-toolbar combobox > .linked > button.combo:dir(ltr):disabled, headerbar combobox > .linked > button.combo:dir(ltr):disabled {
  border-top-left-radius: 0;
  border-bottom-left-radius: 0; }

.primary-toolbar combobox > .linked > button.combo:dir(rtl), headerbar combobox > .linked > button.combo:dir(rtl), .primary-toolbar combobox > .linked > button.combo:dir(rtl):hover, headerbar combobox > .linked > button.combo:dir(rtl):hover, .primary-toolbar combobox > .linked > button.combo:dir(rtl):active, headerbar combobox > .linked > button.combo:dir(rtl):active, .primary-toolbar combobox > .linked > button.combo:dir(rtl):checked, headerbar combobox > .linked > button.combo:dir(rtl):checked, .primary-toolbar combobox > .linked > button.combo:dir(rtl):disabled, headerbar combobox > .linked > button.combo:dir(rtl):disabled {
  border-top-right-radius: 0;
  border-bottom-right-radius: 0; }

.primary-toolbar switch:backdrop, headerbar switch:backdrop {
  opacity: 0.75; }

.primary-toolbar progressbar trough, headerbar progressbar trough {
  background-color: rgba(7, 8, 11, 0.37); }

.primary-toolbar progressbar:backdrop, headerbar progressbar:backdrop {
  opacity: 0.75; }

.primary-toolbar scale:backdrop, headerbar scale:backdrop {
  opacity: 0.75; }

.primary-toolbar scale slider, headerbar scale slider {
  background-color: #333b4f;
  border-color: rgba(7, 8, 11, 0.67); }
  .primary-toolbar scale slider:hover, headerbar scale slider:hover {
    background-color: #3d475e;
    border-color: rgba(7, 8, 11, 0.67); }
  .primary-toolbar scale slider:active, headerbar scale slider:active {
    background-color: """
            + color4
            + """;
    border-color: """
            + color4
            + """; }
  .primary-toolbar scale slider:disabled, headerbar scale slider:disabled {
    background-color: rgba(45, 53, 70, 0.991);
    border-color: rgba(7, 8, 11, 0.67); }

.primary-toolbar scale trough, headerbar scale trough {
  background-color: rgba(7, 8, 11, 0.37); }
  .primary-toolbar scale trough:disabled, headerbar scale trough:disabled {
    background-color: rgba(7, 8, 11, 0.27); }

.path-bar button.text-button, .path-bar button.image-button, .path-bar button {
  padding-left: 6px;
  padding-right: 6px; }

.path-bar button.text-button.image-button label {
  padding-left: 0;
  padding-right: 0; }

.path-bar button.text-button.image-button label:last-child, .path-bar button label:last-child {
  padding-right: 10px; }

.path-bar button.text-button.image-button label:first-child, .path-bar button label:first-child {
  padding-left: 10px; }

.path-bar button.slider-button, .path-bar button:not(.image-button):not(.text-button) {
  padding-left: 1px;
  padding-right: 1px; }

.path-bar button image {
  padding-left: 4px;
  padding-right: 4px; }

treeview.view {
  border-left-color: rgba(203, 204, 198, 0.15);
  border-top-color: rgba(0, 0, 0, 0.1); }
  * {
    -GtkTreeView-horizontal-separator: 4;
    -GtkTreeView-grid-line-width: 1;
    -GtkTreeView-grid-line-pattern: '';
    -GtkTreeView-tree-line-width: 1;
    -GtkTreeView-tree-line-pattern: '';
    -GtkTreeView-expander-size: 16; }
  treeview.view acceleditor > label {
    background-color: """
            + color4
            + """; }
  treeview.view:selected, treeview.view:selected:focus {
    border-radius: 0;
    border-left-color: #808990;
    border-top-color: rgba(203, 204, 198, 0.1); }
  treeview.view:disabled {
    color: rgba(203, 204, 198, 0.45); }
    treeview.view:disabled:selected {
      color: #707b85; }
  treeview.view.separator {
    min-height: 2px;
    color: rgba(0, 0, 0, 0.1); }
  treeview.view:drop(active) {
    border-style: solid none;
    border-width: 1px;
    border-color: #808990; }
    treeview.view:drop(active).after {
      border-top-style: none; }
    treeview.view:drop(active).before {
      border-bottom-style: none; }
  treeview.view.expander {
    -gtk-icon-source: -gtk-icontheme("pan-end-symbolic");
    color: #777a7d; }
    treeview.view.expander:dir(rtl) {
      -gtk-icon-source: -gtk-icontheme("pan-end-symbolic-rtl"); }
    treeview.view.expander:hover {
      color: """
            + color1
            + """; }
    treeview.view.expander:selected {
      color: #9ea4a6; }
      treeview.view.expander:selected:hover {
        color: """
            + color1
            + """; }
    treeview.view.expander:checked {
      -gtk-icon-source: -gtk-icontheme("pan-down-symbolic"); }
  treeview.view.progressbar, treeview.view.progressbar:focus {
    color: """
            + color1
            + """;
    border-radius: 3px;
    background-color: """
            + color4
            + """; }
    treeview.view.progressbar:selected, treeview.view.progressbar:selected:focus, treeview.view.progressbar:focus:selected, treeview.view.progressbar:focus:selected:focus {
      color: """
            + color4
            + """;
      box-shadow: none;
      background-color: """
            + color1
            + """; }
  treeview.view.trough {
    color: """
            + color1
            + """;
    background-color: #13161d;
    border-radius: 3px;
    border-width: 0; }
    treeview.view.trough:selected, treeview.view.trough:selected:focus {
      color: """
            + color1
            + """;
      background-color: rgba(0, 0, 0, 0.2);
      border-radius: 3px;
      border-width: 0; }
  treeview.view header button {
    min-height: 0;
    min-width: 0;
    padding: 3px 6px;
    font-weight: bold;
    color: #a9aba9;
    background-color: """
            + color2
            + """;
    background-image: none;
    border-style: none solid none none;
    border-radius: 0;
    border-image: linear-gradient(to bottom, """
            + color2
            + """ 20%, rgba(255, 255, 255, 0.11) 20%, rgba(255, 255, 255, 0.11) 80%, """
            + color2
            + """ 80%) 0 1 0 0/0 1px 0 0 stretch; }
    treeview.view header button:hover {
      color: """
            + color4
            + """; }
    treeview.view header button:active {
      color: """
            + color1
            + """; }
    treeview.view header button:active, treeview.view header button:hover {
      background-color: """
            + color2
            + """; }
    treeview.view header button:active:hover {
      color: """
            + color1
            + """; }
    treeview.view header button:disabled {
      border-color: """
            + color6
            + """;
      background-image: none; }
    treeview.view header button:last-child {
      border-right-style: none;
      border-image: none; }
  treeview.view button.dnd, treeview.view button.dnd:selected, treeview.view button.dnd:hover, treeview.view button.dnd:active,
  treeview.view header.button.dnd,
  treeview.view header.button.dnd:selected,
  treeview.view header.button.dnd:hover,
  treeview.view header.button.dnd:active {
    padding: 0 6px;
    transition: none;
    color: """
            + color1
            + """;
    background-color: """
            + color4
            + """;
    border-radius: 0;
    border-style: none; }

menubar,
.menubar {
  -GtkWidget-window-dragging: true;
  padding: 0px;
  background-color: """
            + color6
            + """;
  color: rgba(207, 209, 193, 0.8); }
  menubar:backdrop,
  .menubar:backdrop {
    color: rgba(207, 209, 193, 0.5); }
  menubar > menuitem,
  .menubar > menuitem {
    padding: 4px 8px;
    border: solid transparent;
    border-width: 0; }
    menubar > menuitem:hover,
    .menubar > menuitem:hover {
      background-color: """
            + color4
            + """;
      color: """
            + color1
            + """; }
    menubar > menuitem:disabled,
    .menubar > menuitem:disabled {
      color: rgba(207, 209, 193, 0.2);
      border-color: transparent; }

menu,
.menu {
  margin: 4px;
  padding: 0;
  border-radius: 0;
  background-color: """
            + color6
            + """;
  border: 1px solid #13161d; }
  .csd menu, .csd
  .menu {
    padding: 4px 0px;
    border-radius: 2px;
    border: none; }
  menu separator,
  .csd menu separator,
  .menu separator,
  .csd
  .menu separator {
    margin: 2px 0;
    background-color: """
            + color6
            + """; }
  menu .separator:not(label),
  .csd menu .separator:not(label),
  .menu .separator:not(label),
  .csd
  .menu .separator:not(label) {
    color: """
            + color6
            + """; }
  menu menuitem,
  .menu menuitem {
    min-height: 16px;
    min-width: 40px;
    padding: 5px; }
    menu menuitem:hover,
    .menu menuitem:hover {
      color: """
            + color1
            + """;
      background-color: """
            + color4
            + """; }
    menu menuitem:disabled,
    .menu menuitem:disabled {
      color: rgba(203, 204, 198, 0.45); }
    menu menuitem arrow,
    .menu menuitem arrow {
      min-height: 16px;
      min-width: 16px; }
      menu menuitem arrow:dir(ltr),
      .menu menuitem arrow:dir(ltr) {
        -gtk-icon-source: -gtk-icontheme("pan-end-symbolic");
        margin-left: 10px; }
      menu menuitem arrow:dir(rtl),
      .menu menuitem arrow:dir(rtl) {
        -gtk-icon-source: -gtk-icontheme("pan-end-symbolic-rtl");
        margin-right: 10px; }
    menuitem accelerator {
      color: alpha(currentColor,0.55); }
    menuitem check, menuitem radio {
      min-height: 16px;
      min-width: 16px; }
      menuitem check:dir(ltr), menuitem radio:dir(ltr) {
        margin-right: 6px;
        margin-left: 2px; }
      menuitem check:dir(rtl), menuitem radio:dir(rtl) {
        margin-left: 6px;
        margin-right: 2px; }
  menu > arrow,
  .menu > arrow {
    border-color: transparent;
    background-color: transparent;
    background-image: none;
    min-width: 16px;
    min-height: 16px;
    padding: 4px;
    background-color: """
            + color6
            + """;
    border-radius: 0; }
    menu > arrow.top,
    .menu > arrow.top {
      margin-top: -6px;
      border-bottom: 1px solid #343843;
      -gtk-icon-source: -gtk-icontheme("pan-up-symbolic"); }
    menu > arrow.bottom,
    .menu > arrow.bottom {
      margin-bottom: -6px;
      border-top: 1px solid #343843;
      -gtk-icon-source: -gtk-icontheme("pan-down-symbolic"); }
    menu > arrow:hover,
    .menu > arrow:hover {
      background-color: #343843; }
    menu > arrow:disabled,
    .menu > arrow:disabled {
      color: transparent;
      background-color: transparent;
      border-color: transparent; }

popover,
popover.background {
  padding: 2px;
  border-radius: 3px;
  background-clip: border-box;
  background-color: """
            + color6
            + """;
  box-shadow: 0 2px 6px 1px rgba(0, 0, 0, 0.35); }
  .csd popover, popover, .csd
  popover.background,
  popover.background {
    border: 1px solid #090a0e; }
  popover separator,
  popover.background separator {
    background-color: """
            + color6
            + """; }
  popover > list,
  popover > .view,
  popover > iconview,
  popover > toolbar,
  popover > .inline-toolbar,
  popover.background > list,
  popover.background > .view,
  popover.background > iconview,
  popover.background > toolbar,
  popover.background > .inline-toolbar {
    border-style: none;
    background-color: transparent; }

cursor-handle {
  background-color: transparent;
  background-image: none;
  box-shadow: none;
  border-style: none; }
  cursor-handle.top {
    -gtk-icon-source: -gtk-icontheme("selection-start-symbolic"); }
  cursor-handle.bottom {
    -gtk-icon-source: -gtk-icontheme("selection-end-symbolic"); }

notebook {
  padding: 0; }
  notebook.frame {
    border: 1px solid #13161d; }
    notebook.frame > header {
      margin: -1px; }
      notebook.frame > header.top {
        margin-bottom: 0; }
      notebook.frame > header.bottom {
        margin-top: 0; }
      notebook.frame > header.left {
        margin-right: 0; }
      notebook.frame > header.right {
        margin-left: 0; }
      notebook.frame > header.top, notebook.frame > header.bottom {
        padding-left: 0;
        padding-right: 0; }
      notebook.frame > header.left, notebook.frame > header.right {
        padding-top: 0;
        padding-bottom: 0; }
  notebook > stack:not(:only-child) {
    background-color: """
            + color2
            + """; }
  notebook > header {
    padding: 2px;
    background-color: """
            + color6
            + """; }
    notebook > header.top {
      box-shadow: inset 0 -1px #13161d; }
    notebook > header.bottom {
      box-shadow: inset 0 1px #13161d; }
    notebook > header.right {
      box-shadow: inset 1px 0 #13161d; }
    notebook > header.left {
      box-shadow: inset -1px 0 #13161d; }
    notebook > header.top {
      padding-bottom: 0; }
      notebook > header.top > tabs > tab {
        padding: 2px 10px;
        min-width: 20px;
        min-height: 20px;
        outline-offset: -4px;
        border: 1px solid transparent;
        border-bottom: none;
        border-radius: 1px 1px 0 0; }
        notebook > header.top > tabs > tab + tab {
          margin-left: -1px; }
    notebook > header.bottom {
      padding-top: 0; }
      notebook > header.bottom > tabs > tab {
        padding: 2px 10px;
        min-width: 20px;
        min-height: 20px;
        outline-offset: -4px;
        border: 1px solid transparent;
        border-top: none;
        border-radius: 0 0 1px 1px; }
        notebook > header.bottom > tabs > tab + tab {
          margin-left: -1px; }
    notebook > header.right {
      padding-left: 0; }
      notebook > header.right > tabs > tab {
        padding: 2px 10px;
        min-width: 20px;
        min-height: 20px;
        outline-offset: -4px;
        border: 1px solid transparent;
        border-left: none;
        border-radius: 0 1px 1px 0; }
        notebook > header.right > tabs > tab + tab {
          margin-top: -1px; }
    notebook > header.left {
      padding-right: 0; }
      notebook > header.left > tabs > tab {
        padding: 2px 10px;
        min-width: 20px;
        min-height: 20px;
        outline-offset: -4px;
        border: 1px solid transparent;
        border-right: none;
        border-radius: 1px 0 0 1px; }
        notebook > header.left > tabs > tab + tab {
          margin-top: -1px; }
    notebook > header.top > tabs > arrow.up, notebook > header.bottom > tabs > arrow.up {
      -gtk-icon-source: -gtk-icontheme("pan-end-symbolic"); }
      notebook > header.top > tabs > arrow.up:last-child, notebook > header.bottom > tabs > arrow.up:last-child {
        margin-left: 2px; }
    notebook > header.top > tabs > arrow.down, notebook > header.bottom > tabs > arrow.down {
      -gtk-icon-source: -gtk-icontheme("pan-start-symbolic"); }
      notebook > header.top > tabs > arrow.down:first-child, notebook > header.bottom > tabs > arrow.down:first-child {
        margin-right: 2px; }
    notebook > header.left > tabs > arrow.up, notebook > header.right > tabs > arrow.up {
      -gtk-icon-source: -gtk-icontheme("pan-down-symbolic"); }
      notebook > header.left > tabs > arrow.up:last-child, notebook > header.right > tabs > arrow.up:last-child {
        margin-top: 2px; }
    notebook > header.left > tabs > arrow.down, notebook > header.right > tabs > arrow.down {
      -gtk-icon-source: -gtk-icontheme("pan-up-symbolic"); }
      notebook > header.left > tabs > arrow.down:first-child, notebook > header.right > tabs > arrow.down:first-child {
        margin-bottom: 2px; }
    notebook > header > tabs > arrow {
      color: rgba(203, 204, 198, 0.45); }
      notebook > header > tabs > arrow:hover {
        color: rgba(203, 204, 198, 0.725); }
      notebook > header > tabs > arrow:active {
        color: """
            + color1
            + """; }
      notebook > header > tabs > arrow:disabled {
        color: rgba(203, 204, 198, 0.15); }
    notebook > header.top > tabs > tab:hover:not(:checked) {
      box-shadow: inset 0 -1px #13161d; }
    notebook > header.bottom > tabs > tab:hover:not(:checked) {
      box-shadow: inset 0 1px #13161d; }
    notebook > header.left > tabs > tab:hover:not(:checked) {
      box-shadow: inset -1px 0 #13161d; }
    notebook > header.right > tabs > tab:hover:not(:checked) {
      box-shadow: inset 1px 0 #13161d; }
    notebook > header > tabs > tab {
      color: rgba(203, 204, 198, 0.45);
      background-color: rgba(35, 40, 52, 0); }
      notebook > header > tabs > tab:hover:not(:checked) {
        color: rgba(203, 204, 198, 0.725);
        background-color: rgba(35, 40, 52, 0.5);
        border-color: #13161d; }
      notebook > header > tabs > tab:checked {
        color: """
            + color1
            + """;
        background-color: """
            + color2
            + """;
        border-color: #13161d; }
      notebook > header > tabs > tab button.flat, notebook > header > tabs > tab button.sidebar-button {
        min-height: 22px;
        min-width: 16px;
        padding: 0;
        color: #8f9192; }
        notebook > header > tabs > tab button.flat:hover, notebook > header > tabs > tab button.sidebar-button:hover {
          color: #ff4d4d; }
        notebook > header > tabs > tab button.flat:active, notebook > header > tabs > tab button.sidebar-button:active, notebook > header > tabs > tab button.flat:active:hover, notebook > header > tabs > tab button.sidebar-button:active:hover {
          color: """
            + color4
            + """; }

scrollbar {
  background-color: #212631;
  transition: 300ms cubic-bezier(0.25, 0.46, 0.45, 0.94); }
  * {
    -GtkScrollbar-has-backward-stepper: false;
    -GtkScrollbar-has-forward-stepper: false; }
  scrollbar.top {
    border-bottom: 1px solid #13161d; }
  scrollbar.bottom {
    border-top: 1px solid #13161d; }
  scrollbar.left {
    border-right: 1px solid #13161d; }
  scrollbar.right {
    border-left: 1px solid #13161d; }
  scrollbar button {
    border: none; }
  scrollbar.vertical button.down {
    -gtk-icon-source: -gtk-icontheme("pan-down-symbolic"); }
  scrollbar.vertical button.up {
    -gtk-icon-source: -gtk-icontheme("pan-up-symbolic"); }
  scrollbar.horizontal button.down {
    -gtk-icon-source: -gtk-icontheme("pan-right-symbolic"); }
  scrollbar.horizontal button.up {
    -gtk-icon-source: -gtk-icontheme("pan-left-symbolic"); }
  scrollbar slider {
    min-width: 6px;
    min-height: 6px;
    margin: -1px;
    border: 4px solid transparent;
    border-radius: 8px;
    background-clip: padding-box;
    background-color: #64676c; }
    scrollbar slider:hover {
      background-color: #53565d; }
    scrollbar slider:hover:active {
      background-color: """
            + color4
            + """; }
    scrollbar slider:disabled {
      background-color: transparent; }
  scrollbar.fine-tune slider {
    min-width: 4px;
    min-height: 4px; }
  scrollbar.fine-tune.horizontal slider {
    border-width: 5px 4px; }
  scrollbar.fine-tune.vertical slider {
    border-width: 4px 5px; }
  scrollbar.overlay-indicator:not(.dragging):not(.hovering) {
    opacity: 0.4;
    border-color: transparent;
    background-color: transparent; }
    scrollbar.overlay-indicator:not(.dragging):not(.hovering) slider {
      margin: 0;
      min-width: 4px;
      min-height: 4px;
      background-color: #979a99;
      border: 1px solid rgba(0, 0, 0, 0.3); }
    scrollbar.overlay-indicator:not(.dragging):not(.hovering).horizontal slider {
      margin: 0 2px;
      min-width: 40px; }
    scrollbar.overlay-indicator:not(.dragging):not(.hovering).vertical slider {
      margin: 2px 0;
      min-height: 40px; }
  scrollbar.overlay-indicator.dragging, scrollbar.overlay-indicator.hovering {
    opacity: 0.99; }
  scrollbar.horizontal slider {
    min-width: 40px; }
  scrollbar.vertical slider {
    min-height: 40px; }

switch {
  font-size: 1px;
  min-width: 52px;
  min-height: 24px;
  background-size: 52px 24px;
  background-repeat: no-repeat;
  background-position: center center; }
  switch slider {
    min-width: 1px;
    min-height: 1px; }
  switch, switch slider {
    outline-color: transparent;
    color: transparent;
    border: none;
    box-shadow: none; }

switch {
  background-image: -gtk-scaled(url("assets/switch-dark.png"), url("assets/switch-dark@2.png")); }

menuitem:hover switch,
row:selected switch,
infobar switch {
  background-image: -gtk-scaled(url("assets/switch-selected.png"), url("assets/switch-selected@2.png")); }

headerbar switch,
.primary-toolbar switch {
  background-image: -gtk-scaled(url("assets/switch-header-dark.png"), url("assets/switch-header-dark@2.png")); }

switch:checked {
  background-image: -gtk-scaled(url("assets/switch-active-dark.png"), url("assets/switch-active-dark@2.png")); }

menuitem:hover switch:checked,
row:selected switch:checked,
infobar switch:checked {
  background-image: -gtk-scaled(url("assets/switch-active-selected.png"), url("assets/switch-active-selected@2.png")); }

headerbar switch:checked,
.primary-toolbar switch:checked {
  background-image: -gtk-scaled(url("assets/switch-active-header-dark.png"), url("assets/switch-active-header-dark@2.png")); }

switch:disabled {
  background-image: -gtk-scaled(url("assets/switch-insensitive-dark.png"), url("assets/switch-insensitive-dark@2.png")); }

menuitem:hover switch:disabled,
row:selected switch:disabled,
infobar switch:disabled {
  background-image: -gtk-scaled(url("assets/switch-insensitive-selected.png"), url("assets/switch-insensitive-selected@2.png")); }

headerbar switch:disabled,
.primary-toolbar switch:disabled {
  background-image: -gtk-scaled(url("assets/switch-insensitive-header-dark.png"), url("assets/switch-insensitive-header-dark@2.png")); }

switch:checked:disabled {
  background-image: -gtk-scaled(url("assets/switch-active-insensitive-dark.png"), url("assets/switch-active-insensitive-dark@2.png")); }

menuitem:hover switch:checked:disabled,
row:selected switch:checked:disabled,
infobar switch:checked:disabled {
  background-image: -gtk-scaled(url("assets/switch-active-insensitive-selected.png"), url("assets/switch-active-insensitive-selected@2.png")); }

headerbar switch:checked:disabled,
.primary-toolbar switch:checked:disabled {
  background-image: -gtk-scaled(url("assets/switch-active-insensitive-header-dark.png"), url("assets/switch-active-insensitive-header-dark@2.png")); }

.check,
check,
treeview.check {
  -gtk-icon-source: -gtk-scaled(url("assets/checkbox-unchecked-dark.png"), url("assets/checkbox-unchecked-dark@2.png")); }

.osd check, filechooser actionbar check {
  -gtk-icon-source: -gtk-scaled(url("assets/checkbox-unchecked-dark.png"), url("assets/checkbox-unchecked-dark@2.png")); }

menuitem check:hover,
.view check:selected, iconview check:selected,
treeview.check:selected,
row:selected check,
infobar check {
  -gtk-icon-source: -gtk-scaled(url("assets/checkbox-unchecked-selected.png"), url("assets/checkbox-unchecked-selected@2.png")); }

.check:disabled,
check:disabled,
treeview.check:disabled {
  -gtk-icon-source: -gtk-scaled(url("assets/checkbox-unchecked-insensitive-dark.png"), url("assets/checkbox-unchecked-insensitive-dark@2.png")); }

.osd check:disabled, filechooser actionbar check:disabled {
  -gtk-icon-source: -gtk-scaled(url("assets/checkbox-unchecked-insensitive-dark.png"), url("assets/checkbox-unchecked-insensitive-dark@2.png")); }

menuitem check:disabled:hover,
.view check:disabled:selected, iconview check:disabled:selected,
treeview.check:disabled:selected,
row:selected check:disabled,
infobar check:disabled {
  -gtk-icon-source: -gtk-scaled(url("assets/checkbox-unchecked-insensitive-selected.png"), url("assets/checkbox-unchecked-insensitive-selected@2.png")); }

.check:indeterminate,
check:indeterminate,
treeview.check:indeterminate {
  -gtk-icon-source: -gtk-scaled(url("assets/checkbox-mixed-dark.png"), url("assets/checkbox-mixed-dark@2.png")); }

.osd check:indeterminate, filechooser actionbar check:indeterminate {
  -gtk-icon-source: -gtk-scaled(url("assets/checkbox-mixed-dark.png"), url("assets/checkbox-mixed-dark@2.png")); }

menuitem check:indeterminate:hover,
.view check:indeterminate:selected, iconview check:indeterminate:selected,
treeview.check:indeterminate:selected,
row:selected check:indeterminate,
infobar check:indeterminate {
  -gtk-icon-source: -gtk-scaled(url("assets/checkbox-mixed-selected.png"), url("assets/checkbox-mixed-selected@2.png")); }

.check:indeterminate:disabled,
check:indeterminate:disabled,
treeview.check:indeterminate:disabled {
  -gtk-icon-source: -gtk-scaled(url("assets/checkbox-mixed-insensitive-dark.png"), url("assets/checkbox-mixed-insensitive-dark@2.png")); }

.osd check:indeterminate:disabled, filechooser actionbar check:indeterminate:disabled {
  -gtk-icon-source: -gtk-scaled(url("assets/checkbox-mixed-insensitive-dark.png"), url("assets/checkbox-mixed-insensitive-dark@2.png")); }

menuitem check:indeterminate:disabled:hover,
.view check:indeterminate:disabled:selected, iconview check:indeterminate:disabled:selected,
treeview.check:indeterminate:disabled:selected,
row:selected check:indeterminate:disabled,
infobar check:indeterminate:disabled {
  -gtk-icon-source: -gtk-scaled(url("assets/checkbox-mixed-insensitive-selected.png"), url("assets/checkbox-mixed-insensitive-selected@2.png")); }

.check:checked,
check:checked,
treeview.check:checked {
  -gtk-icon-source: -gtk-scaled(url("assets/checkbox-checked-dark.png"), url("assets/checkbox-checked-dark@2.png")); }

.osd check:checked, filechooser actionbar check:checked {
  -gtk-icon-source: -gtk-scaled(url("assets/checkbox-checked-dark.png"), url("assets/checkbox-checked-dark@2.png")); }

menuitem check:checked:hover,
.view check:checked:selected, iconview check:checked:selected,
treeview.check:checked:selected,
row:selected check:checked,
infobar check:checked {
  -gtk-icon-source: -gtk-scaled(url("assets/checkbox-checked-selected.png"), url("assets/checkbox-checked-selected@2.png")); }

.check:checked:disabled,
check:checked:disabled,
treeview.check:checked:disabled {
  -gtk-icon-source: -gtk-scaled(url("assets/checkbox-checked-insensitive-dark.png"), url("assets/checkbox-checked-insensitive-dark@2.png")); }

.osd check:checked:disabled, filechooser actionbar check:checked:disabled {
  -gtk-icon-source: -gtk-scaled(url("assets/checkbox-checked-insensitive-dark.png"), url("assets/checkbox-checked-insensitive-dark@2.png")); }

menuitem check:checked:disabled:hover,
.view check:checked:disabled:selected, iconview check:checked:disabled:selected,
treeview.check:checked:disabled:selected,
row:selected check:checked:disabled,
infobar check:checked:disabled {
  -gtk-icon-source: -gtk-scaled(url("assets/checkbox-checked-insensitive-selected.png"), url("assets/checkbox-checked-insensitive-selected@2.png")); }

.radio,
radio,
treeview.radio {
  -gtk-icon-source: -gtk-scaled(url("assets/radio-unchecked-dark.png"), url("assets/radio-unchecked-dark@2.png")); }

.osd radio, filechooser actionbar radio {
  -gtk-icon-source: -gtk-scaled(url("assets/radio-unchecked-dark.png"), url("assets/radio-unchecked-dark@2.png")); }

menuitem radio:hover,
.view radio:selected, iconview radio:selected,
treeview.radio:selected,
row:selected radio,
infobar radio {
  -gtk-icon-source: -gtk-scaled(url("assets/radio-unchecked-selected.png"), url("assets/radio-unchecked-selected@2.png")); }

.radio:disabled,
radio:disabled,
treeview.radio:disabled {
  -gtk-icon-source: -gtk-scaled(url("assets/radio-unchecked-insensitive-dark.png"), url("assets/radio-unchecked-insensitive-dark@2.png")); }

.osd radio:disabled, filechooser actionbar radio:disabled {
  -gtk-icon-source: -gtk-scaled(url("assets/radio-unchecked-insensitive-dark.png"), url("assets/radio-unchecked-insensitive-dark@2.png")); }

menuitem radio:disabled:hover,
.view radio:disabled:selected, iconview radio:disabled:selected,
treeview.radio:disabled:selected,
row:selected radio:disabled,
infobar radio:disabled {
  -gtk-icon-source: -gtk-scaled(url("assets/radio-unchecked-insensitive-selected.png"), url("assets/radio-unchecked-insensitive-selected@2.png")); }

.radio:indeterminate,
radio:indeterminate,
treeview.radio:indeterminate {
  -gtk-icon-source: -gtk-scaled(url("assets/radio-mixed-dark.png"), url("assets/radio-mixed-dark@2.png")); }

.osd radio:indeterminate, filechooser actionbar radio:indeterminate {
  -gtk-icon-source: -gtk-scaled(url("assets/radio-mixed-dark.png"), url("assets/radio-mixed-dark@2.png")); }

menuitem radio:indeterminate:hover,
.view radio:indeterminate:selected, iconview radio:indeterminate:selected,
treeview.radio:indeterminate:selected,
row:selected radio:indeterminate,
infobar radio:indeterminate {
  -gtk-icon-source: -gtk-scaled(url("assets/radio-mixed-selected.png"), url("assets/radio-mixed-selected@2.png")); }

.radio:indeterminate:disabled,
radio:indeterminate:disabled,
treeview.radio:indeterminate:disabled {
  -gtk-icon-source: -gtk-scaled(url("assets/radio-mixed-insensitive-dark.png"), url("assets/radio-mixed-insensitive-dark@2.png")); }

.osd radio:indeterminate:disabled, filechooser actionbar radio:indeterminate:disabled {
  -gtk-icon-source: -gtk-scaled(url("assets/radio-mixed-insensitive-dark.png"), url("assets/radio-mixed-insensitive-dark@2.png")); }

menuitem radio:indeterminate:disabled:hover,
.view radio:indeterminate:disabled:selected, iconview radio:indeterminate:disabled:selected,
treeview.radio:indeterminate:disabled:selected,
row:selected radio:indeterminate:disabled,
infobar radio:indeterminate:disabled {
  -gtk-icon-source: -gtk-scaled(url("assets/radio-mixed-insensitive-selected.png"), url("assets/radio-mixed-insensitive-selected@2.png")); }

.radio:checked,
radio:checked,
treeview.radio:checked {
  -gtk-icon-source: -gtk-scaled(url("assets/radio-checked-dark.png"), url("assets/radio-checked-dark@2.png")); }

.osd radio:checked, filechooser actionbar radio:checked {
  -gtk-icon-source: -gtk-scaled(url("assets/radio-checked-dark.png"), url("assets/radio-checked-dark@2.png")); }

menuitem radio:checked:hover,
.view radio:checked:selected, iconview radio:checked:selected,
treeview.radio:checked:selected,
row:selected radio:checked,
infobar radio:checked {
  -gtk-icon-source: -gtk-scaled(url("assets/radio-checked-selected.png"), url("assets/radio-checked-selected@2.png")); }

.radio:checked:disabled,
radio:checked:disabled,
treeview.radio:checked:disabled {
  -gtk-icon-source: -gtk-scaled(url("assets/radio-checked-insensitive-dark.png"), url("assets/radio-checked-insensitive-dark@2.png")); }

.osd radio:checked:disabled, filechooser actionbar radio:checked:disabled {
  -gtk-icon-source: -gtk-scaled(url("assets/radio-checked-insensitive-dark.png"), url("assets/radio-checked-insensitive-dark@2.png")); }

menuitem radio:checked:disabled:hover,
.view radio:checked:disabled:selected, iconview radio:checked:disabled:selected,
treeview.radio:checked:disabled:selected,
row:selected radio:checked:disabled,
infobar radio:checked:disabled {
  -gtk-icon-source: -gtk-scaled(url("assets/radio-checked-insensitive-selected.png"), url("assets/radio-checked-insensitive-selected@2.png")); }

.view.content-view.check:not(list), iconview.content-view.check:not(list) {
  -gtk-icon-source: -gtk-scaled(url("assets/checkbox-selectionmode-dark.png"), url("assets/checkbox-selectionmode-dark@2.png"));
  background-color: transparent; }

.view.content-view.check:checked:not(list), iconview.content-view.check:checked:not(list) {
  -gtk-icon-source: -gtk-scaled(url("assets/checkbox-checked-selectionmode-dark.png"), url("assets/checkbox-checked-selectionmode-dark@2.png"));
  background-color: transparent; }

checkbutton.text-button, radiobutton.text-button {
  padding: 2px 0;
  outline-offset: 0; }

checkbutton label:not(:only-child):first-child, radiobutton label:not(:only-child):first-child {
  margin-left: 4px; }

checkbutton label:not(:only-child):last-child, radiobutton label:not(:only-child):last-child {
  margin-right: 4px; }

check,
radio {
  min-width: 16px;
  min-height: 16px;
  margin: 0 2px; }
  check:only-child,
  menu menuitem check,
  radio:only-child,
  menu menuitem
  radio {
    margin: 0; }

scale {
  min-height: 15px;
  min-width: 15px;
  padding: 3px; }
  scale.horizontal trough {
    padding: 0 4px; }
  scale.horizontal highlight, scale.horizontal fill {
    margin: 0 -4px; }
  scale.vertical trough {
    padding: 4px 0; }
  scale.vertical highlight, scale.vertical fill {
    margin: -4px 0; }
  scale slider {
    min-height: 15px;
    min-width: 15px;
    margin: -6px; }
  scale.fine-tune slider {
    margin: -4px; }
  scale.fine-tune fill,
  scale.fine-tune highlight,
  scale.fine-tune trough {
    border-radius: 5px;
    -gtk-outline-radius: 7px; }
  scale trough {
    outline-offset: 2px;
    -gtk-outline-radius: 4.5px;
    border-radius: 2.5px;
    background-color: #151821; }
    scale trough:disabled {
      background-color: rgba(21, 24, 33, 0.55); }
    .osd scale trough {
      background-color: rgba(49, 56, 73, 0.95); }
      .osd scale trough highlight {
        background-color: """
            + color4
            + """; }
    menuitem:hover scale trough,
    row:selected scale trough,
    infobar scale trough {
      background-color: rgba(0, 0, 0, 0.2); }
      menuitem:hover scale trough highlight,
      row:selected scale trough highlight,
      infobar scale trough highlight {
        background-color: """
            + color1
            + """; }
        menuitem:hover scale trough highlight:disabled,
        row:selected scale trough highlight:disabled,
        infobar scale trough highlight:disabled {
          background-color: #878f95; }
      menuitem:hover scale trough:disabled,
      row:selected scale trough:disabled,
      infobar scale trough:disabled {
        background-color: rgba(0, 0, 0, 0.1); }
  scale highlight {
    border-radius: 2.5px;
    background-color: """
            + color4
            + """; }
    scale highlight:disabled {
      background-color: rgba(52, 69, 90, 0.55); }
  scale fill {
    border-radius: 2.5px;
    background-color: rgba(52, 69, 90, 0.5); }
    scale fill:disabled {
      background-color: transparent; }
  scale slider {
    background-color: """
            + color5
            + """;
    border: 1px solid #0f1117;
    border-radius: 100%;
    transition: all 200ms cubic-bezier(0.25, 0.46, 0.45, 0.94);
    transition-property: background, border; }
    scale slider:hover {
      background-color: #313849; }
    scale slider:active {
      background-clip: border-box;
      background-color: """
            + color4
            + """;
      border-color: """
            + color4
            + """; }
    scale slider:disabled {
      background-color: """
            + color3
            + """;
      border-color: rgba(15, 17, 23, 0.8); }
    menuitem:hover scale slider,
    row:selected scale slider,
    infobar scale slider {
      background-clip: border-box;
      background-color: """
            + color1
            + """;
      border-color: """
            + color1
            + """; }
      menuitem:hover scale slider:hover,
      row:selected scale slider:hover,
      infobar scale slider:hover {
        background-color: #b4b8b6;
        border-color: #b4b8b6; }
      menuitem:hover scale slider:active,
      row:selected scale slider:active,
      infobar scale slider:active {
        background-color: #808990;
        border-color: #808990; }
      menuitem:hover scale slider:disabled,
      row:selected scale slider:disabled,
      infobar scale slider:disabled {
        background-color: #878f95;
        border-color: #878f95; }
    .osd scale slider {
      background-clip: border-box;
      background-color: """
            + color4
            + """;
      border-color: """
            + color4
            + """; }
      .osd scale slider:hover {
        background-color: #475e7a;
        border-color: #475e7a; }
      .osd scale slider:active {
        background-color: #212c3a;
        border-color: #212c3a; }
  scale value {
    color: alpha(currentColor,0.4); }
  scale marks {
    color: alpha(currentColor,0.4); }
    scale marks.top {
      margin-bottom: 1px;
      margin-top: -4px; }
    scale marks.bottom {
      margin-top: 1px;
      margin-bottom: -4px; }
    scale marks.top {
      margin-right: 1px;
      margin-left: -4px; }
    scale marks.bottom {
      margin-left: 1px;
      margin-right: -4px; }
  scale.fine-tune marks.top {
    margin-bottom: 0px;
    margin-top: -2px; }
  scale.fine-tune marks.bottom {
    margin-top: 0px;
    margin-bottom: -2px; }
  scale.fine-tune marks.top {
    margin-right: 0px;
    margin-left: -2px; }
  scale.fine-tune marks.bottom {
    margin-left: 0px;
    margin-right: -2px; }
  scale.horizontal indicator {
    min-height: 3px;
    min-width: 1px; }
  scale.horizontal.fine-tune indicator {
    min-height: 2px; }
  scale.vertical indicator {
    min-height: 1px;
    min-width: 3px; }
  scale.vertical.fine-tune indicator {
    min-width: 2px; }

progressbar {
  padding: 0;
  font-size: smaller;
  color: rgba(203, 204, 198, 0.7); }
  progressbar.osd {
    min-width: 3px;
    min-height: 3px;
    background-color: transparent; }
    progressbar.osd trough {
      border-style: none;
      background-color: transparent;
      box-shadow: none; }
  progressbar progress {
    background-color: """
            + color4
            + """;
    border: none;
    border-radius: 3px;
    box-shadow: none; }
    row:selected progressbar progress,
    infobar progressbar progress {
      background-color: """
            + color1
            + """; }
  progressbar trough {
    border: none;
    border-radius: 3px;
    background-color: #151821; }
    row:selected progressbar trough,
    infobar progressbar trough {
      background-color: rgba(0, 0, 0, 0.2); }

levelbar block {
  min-width: 32px;
  min-height: 1px; }

levelbar.vertical block {
  min-width: 1px;
  min-height: 32px; }

levelbar trough {
  border: none;
  padding: 3px;
  border-radius: 3px;
  background-color: #151821; }

levelbar.horizontal.discrete block {
  margin: 0 1px; }

levelbar.vertical.discrete block {
  margin: 1px 0; }

levelbar block:not(.empty) {
  border: 1px solid """
            + color4
            + """;
  background-color: """
            + color4
            + """;
  border-radius: 2px; }

levelbar block.low {
  border-color: #F27835;
  background-color: #F27835; }

levelbar block.high {
  border-color: """
            + color4
            + """;
  background-color: """
            + color4
            + """; }

levelbar block.full {
  border-color: #73d216;
  background-color: #73d216; }

levelbar block.empty {
  background-color: """
            + color2
            + """;
  border-color: """
            + color2
            + """; }

printdialog paper {
  border: 1px solid #13161d;
  background: """
            + color2
            + """;
  padding: 0; }

printdialog .dialog-action-box {
  margin: 12px; }

frame > border,
.frame {
  margin: 0;
  padding: 0;
  border-radius: 0;
  border: 1px solid #13161d; }

frame.flat > border,
frame > border.flat,
.frame.flat {
  border-style: none; }

scrolledwindow viewport.frame {
  border-style: none; }

scrolledwindow overshoot.top {
  background-image: -gtk-gradient(radial, center top, 0, center top, 0.6, from(rgba(52, 69, 90, 0.2)), to(rgba(52, 69, 90, 0)));
  background-size: 100% 60%;
  background-repeat: no-repeat;
  background-position: center top;
  background-color: transparent;
  border: none;
  box-shadow: none; }

scrolledwindow overshoot.bottom {
  background-image: -gtk-gradient(radial, center bottom, 0, center bottom, 0.6, from(rgba(52, 69, 90, 0.2)), to(rgba(52, 69, 90, 0)));
  background-size: 100% 60%;
  background-repeat: no-repeat;
  background-position: center bottom;
  background-color: transparent;
  border: none;
  box-shadow: none; }

scrolledwindow overshoot.left {
  background-image: -gtk-gradient(radial, left center, 0, left center, 0.6, from(rgba(52, 69, 90, 0.2)), to(rgba(52, 69, 90, 0)));
  background-size: 60% 100%;
  background-repeat: no-repeat;
  background-position: left center;
  background-color: transparent;
  border: none;
  box-shadow: none; }

scrolledwindow overshoot.right {
  background-image: -gtk-gradient(radial, right center, 0, right center, 0.6, from(rgba(52, 69, 90, 0.2)), to(rgba(52, 69, 90, 0)));
  background-size: 60% 100%;
  background-repeat: no-repeat;
  background-position: right center;
  background-color: transparent;
  border: none;
  box-shadow: none; }

scrolledwindow undershoot.top {
  background-color: transparent;
  background-image: linear-gradient(to left, rgba(255, 255, 255, 0.2) 50%, rgba(0, 0, 0, 0.2) 50%);
  padding-top: 1px;
  background-size: 10px 1px;
  background-repeat: repeat-x;
  background-origin: content-box;
  background-position: center top;
  border: none; }

scrolledwindow undershoot.bottom {
  background-color: transparent;
  background-image: linear-gradient(to left, rgba(255, 255, 255, 0.2) 50%, rgba(0, 0, 0, 0.2) 50%);
  padding-bottom: 1px;
  background-size: 10px 1px;
  background-repeat: repeat-x;
  background-origin: content-box;
  background-position: center bottom;
  border: none; }

scrolledwindow undershoot.left {
  background-color: transparent;
  background-image: linear-gradient(to top, rgba(255, 255, 255, 0.2) 50%, rgba(0, 0, 0, 0.2) 50%);
  padding-left: 1px;
  background-size: 1px 10px;
  background-repeat: repeat-y;
  background-origin: content-box;
  background-position: left center;
  border: none; }

scrolledwindow undershoot.right {
  background-color: transparent;
  background-image: linear-gradient(to top, rgba(255, 255, 255, 0.2) 50%, rgba(0, 0, 0, 0.2) 50%);
  padding-right: 1px;
  background-size: 1px 10px;
  background-repeat: repeat-y;
  background-origin: content-box;
  background-position: right center;
  border: none; }

scrolledwindow junction {
  border-color: transparent;
  border-image: linear-gradient(to bottom, #13161d 1px, transparent 1px) 0 0 0 1/0 1px stretch;
  background-color: #212631; }
  scrolledwindow junction:dir(rtl) {
    border-image-slice: 0 1 0 0; }

separator {
  background-color: rgba(0, 0, 0, 0.1);
  min-width: 1px;
  min-height: 1px; }

list {
  background-color: """
            + color2
            + """;
  border-color: #13161d; }
  list row {
    padding: 2px; }

row:not(:hover) {
  transition: all 150ms cubic-bezier(0.25, 0.46, 0.45, 0.94); }

row.activatable.has-open-popup, row.activatable:hover {
  background-color: rgba(255, 255, 255, 0.03); }

row.activatable:active {
  color: """
            + color1
            + """; }

row.activatable:disabled {
  color: rgba(203, 204, 198, 0.45); }
  row.activatable:disabled image {
    color: inherit; }

row.activatable:selected:active {
  color: """
            + color1
            + """; }

row.activatable:selected.has-open-popup, row.activatable:selected:hover {
  background-color: #2f3e51; }

.app-notification {
  padding: 10px;
  color: """
            + color1
            + """;
  background-color: rgba(35, 40, 52, 0.95);
  background-clip: border-box;
  border-radius: 0 0 2px 2px;
  border-width: 0 1px 1px 1px;
  border-style: solid;
  border-color: rgba(14, 17, 22, 0.95); }
  .app-notification border {
    border: none; }
  .app-notification button {
    color: """
            + color1
            + """;
    border-color: rgba(10, 12, 15, 0.35);
    background-color: rgba(80, 92, 119, 0.35); }
    .app-notification button.flat, .app-notification button.sidebar-button {
      border-color: rgba(52, 69, 90, 0); }
    .app-notification button:hover {
      color: """
            + color1
            + """;
      border-color: rgba(10, 12, 15, 0.35);
      background-color: rgba(95, 108, 140, 0.45); }
    .app-notification button:active, .app-notification button:checked {
      color: """
            + color1
            + """;
      border-color: rgba(10, 12, 15, 0.35);
      background-color: """
            + color4
            + """;
      background-clip: padding-box; }
    .app-notification button:disabled {
      color: #555960;
      border-color: rgba(10, 12, 15, 0.35);
      background-color: rgba(80, 92, 119, 0.2); }

expander arrow {
  min-width: 16px;
  min-height: 16px;
  -gtk-icon-source: -gtk-icontheme("pan-end-symbolic"); }
  expander arrow:dir(rtl) {
    -gtk-icon-source: -gtk-icontheme("pan-end-symbolic-rtl"); }
  expander arrow:hover {
    color: white; }
  expander arrow:checked {
    -gtk-icon-source: -gtk-icontheme("pan-down-symbolic"); }

calendar {
  color: """
            + color1
            + """;
  border: 1px solid #13161d;
  border-radius: 3px;
  padding: 2px; }
  calendar:selected {
    border-radius: 1.5px; }
  calendar.header {
    color: """
            + color1
            + """;
    border: none; }
  calendar.button {
    color: rgba(203, 204, 198, 0.45); }
    calendar.button:hover {
      color: """
            + color1
            + """; }
    calendar.button:disabled {
      color: rgba(203, 204, 198, 0.45); }
  calendar:indeterminate {
    color: alpha(currentColor,0.55); }
  calendar.highlight {
    color: """
            + color1
            + """; }

messagedialog .titlebar {
  min-height: 20px;
  background-color: rgba(31, 36, 48, 0.97);
  border-bottom: 1px solid rgba(17, 20, 26, 0.97); }

messagedialog .dialog-action-area button {
  padding: 8px;
  min-height: 0; }

messagedialog.csd.background {
  border-bottom-left-radius: 3px;
  border-bottom-right-radius: 3px;
  border: none; }

messagedialog.csd .dialog-action-area button {
  border-bottom-style: none; }

messagedialog.csd .dialog-action-area button {
  border-radius: 0;
  border-right-style: none; }

messagedialog.csd .dialog-action-area button:last-child {
  border-radius: 0 0 3px 0;
  border-right-style: none; }

messagedialog.csd .dialog-action-area button:first-child {
  border-radius: 0 0 0 3px;
  border-left-style: none; }

messagedialog.csd .dialog-action-area button:only-child {
  border-radius: 0 0 3px 3px;
  border-left-style: none;
  border-right-style: none; }

filechooser #pathbarbox {
  border-bottom: 1px solid rgba(19, 22, 29, 0.5); }

filechooserbutton:drop(active) {
  box-shadow: none;
  border-color: transparent; }

.sidebar {
  border-style: none;
  background-color: #232936; }
  stacksidebar.sidebar:dir(ltr) list,
  stacksidebar.sidebar.left list,
  stacksidebar.sidebar.left:dir(rtl) list, .sidebar:dir(ltr), .sidebar.left, .sidebar.left:dir(rtl) {
    border-right: 1px solid #13161d;
    border-left-style: none; }
  stacksidebar.sidebar:dir(rtl) list,
  stacksidebar.sidebar.right list, .sidebar:dir(rtl), .sidebar.right {
    border-left: 1px solid #13161d;
    border-right-style: none; }
  .sidebar list {
    background-color: transparent; }
  paned .sidebar.left, paned .sidebar.right, paned .sidebar.left:dir(rtl), paned .sidebar:dir(rtl), paned .sidebar:dir(ltr), paned .sidebar {
    border-style: none; }

stacksidebar row {
  padding: 10px 4px; }
  stacksidebar row > label {
    padding-left: 6px;
    padding-right: 6px; }
  stacksidebar row.needs-attention > label {
    background-size: 6px 6px, 0 0; }

placessidebar > viewport.frame {
  border-style: none; }

placessidebar row {
  min-height: 30px;
  padding: 0px; }
  placessidebar row > revealer {
    padding: 0 10px; }
  placessidebar row image.sidebar-icon:dir(ltr) {
    padding-right: 8px; }
  placessidebar row image.sidebar-icon:dir(rtl) {
    padding-left: 8px; }
  placessidebar row label.sidebar-label:dir(ltr) {
    padding-right: 2px; }
  placessidebar row label.sidebar-label:dir(rtl) {
    padding-left: 2px; }
  button.sidebar-button {
    min-width: 22px;
    min-height: 22px;
    margin-top: 2px;
    margin-bottom: 2px;
    padding: 0;
    border-radius: 100%;
    -gtk-outline-radius: 100%; }
    button.sidebar-button:not(:hover):not(:active) > image {
      opacity: 0.5; }
  placessidebar row.sidebar-placeholder-row {
    padding: 0 8px;
    min-height: 2px;
    background-image: linear-gradient(to bottom, #F08437, #F08437);
    background-clip: content-box; }
  placessidebar row.sidebar-new-bookmark-row {
    color: """
            + color4
            + """; }
  placessidebar row:drop(active):not(:disabled) {
    box-shadow: inset 0 1px #F08437, inset 0 -1px #F08437; }
    placessidebar row:drop(active):not(:disabled), placessidebar row:drop(active):not(:disabled) label, placessidebar row:drop(active):not(:disabled) image {
      color: #F08437; }
    placessidebar row:drop(active):not(:disabled):selected {
      background-color: #F08437; }
      placessidebar row:drop(active):not(:disabled):selected, placessidebar row:drop(active):not(:disabled):selected label, placessidebar row:drop(active):not(:disabled):selected image {
        color: """
            + color1
            + """; }

placesview .server-list-button > image {
  -gtk-icon-transform: rotate(0turn); }

placesview .server-list-button:checked > image {
  transition: 200ms cubic-bezier(0.25, 0.46, 0.45, 0.94);
  -gtk-icon-transform: rotate(-0.5turn); }

placesview > actionbar > revealer > box > label {
  padding-left: 8px;
  padding-right: 8px; }

paned > separator {
  min-width: 1px;
  min-height: 1px;
  -gtk-icon-source: none;
  border-style: none;
  background-color: transparent;
  background-image: linear-gradient(to bottom, #13161d, #13161d);
  background-size: 1px 1px; }
  paned > separator:selected {
    background-image: linear-gradient(to bottom, """
            + color4
            + """, """
            + color4
            + """); }
  paned > separator.wide {
    min-width: 5px;
    min-height: 5px;
    background-color: """
            + color6
            + """;
    background-image: linear-gradient(to bottom, #13161d, #13161d), linear-gradient(to bottom, #13161d, #13161d);
    background-size: 1px 1px, 1px 1px; }

paned.horizontal > separator {
  background-repeat: repeat-y; }
  paned.horizontal > separator:dir(ltr) {
    margin: 0 -8px 0 0;
    padding: 0 8px 0 0;
    background-position: left; }
  paned.horizontal > separator:dir(rtl) {
    margin: 0 0 0 -8px;
    padding: 0 0 0 8px;
    background-position: right; }
  paned.horizontal > separator.wide {
    margin: 0;
    padding: 0;
    background-repeat: repeat-y, repeat-y;
    background-position: left, right; }

paned.vertical > separator {
  margin: 0 0 -8px 0;
  padding: 0 0 8px 0;
  background-repeat: repeat-x;
  background-position: top; }
  paned.vertical > separator.wide {
    margin: 0;
    padding: 0;
    background-repeat: repeat-x, repeat-x;
    background-position: bottom, top; }

infobar {
  border-style: none; }
  infobar.info, infobar.question, infobar.warning, infobar.error {
    background-color: """
            + color4
            + """;
    color: """
            + color1
            + """;
    caret-color: currentColor; }
    infobar.info selection, infobar.question selection, infobar.warning selection, infobar.error selection {
      color: """
            + color4
            + """;
      background-color: """
            + color1
            + """; }

.selection-mode.primary-toolbar button:hover, headerbar.selection-mode button:hover, row:selected button, infobar.info button, infobar.question button, infobar.warning button, infobar.error button, .nautilus-window .floating-bar button {
  color: """
            + color1
            + """;
  background-color: rgba(203, 204, 198, 0);
  border-color: rgba(203, 204, 198, 0.5); }

row:selected button.flat, row:selected button.sidebar-button, infobar.info button.flat, infobar.info button.sidebar-button, infobar.question button.flat, infobar.question button.sidebar-button, infobar.warning button.flat, infobar.warning button.sidebar-button, infobar.error button.flat, infobar.error button.sidebar-button, .nautilus-window .floating-bar button.flat, .nautilus-window .floating-bar button.sidebar-button {
  border-color: transparent;
  background-color: transparent;
  background-image: none;
  color: """
            + color1
            + """;
  background-color: rgba(203, 204, 198, 0); }
  .selection-mode.primary-toolbar button:disabled, headerbar.selection-mode button:disabled, row:selected button.flat:disabled, row:selected button.sidebar-button:disabled, infobar.info button.flat:disabled, infobar.info button.sidebar-button:disabled, infobar.question button.flat:disabled, infobar.question button.sidebar-button:disabled, infobar.warning button.flat:disabled, infobar.warning button.sidebar-button:disabled, infobar.error button.flat:disabled, infobar.error button.sidebar-button:disabled, .nautilus-window .floating-bar button.flat:disabled, .nautilus-window .floating-bar button.sidebar-button:disabled, .selection-mode.primary-toolbar button:disabled label, headerbar.selection-mode button:disabled label, row:selected button.flat:disabled label, row:selected button.sidebar-button:disabled label, infobar.info button.flat:disabled label, infobar.info button.sidebar-button:disabled label, infobar.question button.flat:disabled label, infobar.question button.sidebar-button:disabled label, infobar.warning button.flat:disabled label, infobar.warning button.sidebar-button:disabled label, infobar.error button.flat:disabled label, infobar.error button.sidebar-button:disabled label, .nautilus-window .floating-bar button.flat:disabled label, .nautilus-window .floating-bar button.sidebar-button:disabled label {
    color: rgba(203, 204, 198, 0.4); }

row:selected button:hover, infobar.info button:hover, infobar.question button:hover, infobar.warning button:hover, infobar.error button:hover, .nautilus-window .floating-bar button:hover {
  color: """
            + color1
            + """;
  background-color: rgba(203, 204, 198, 0.2);
  border-color: rgba(203, 204, 198, 0.8); }

.selection-mode.primary-toolbar button:active, headerbar.selection-mode button:active, .selection-mode.primary-toolbar button:checked, headerbar.selection-mode button:checked, row:selected button:active, infobar.info button:active, infobar.question button:active, infobar.warning button:active, infobar.error button:active, .nautilus-window .floating-bar button:active, .selection-mode.primary-toolbar button:hover:active, headerbar.selection-mode button:hover:active, .selection-mode.primary-toolbar button:hover:checked, headerbar.selection-mode button:hover:checked, row:selected button:active:hover, infobar.info button:active:hover, infobar.question button:active:hover, infobar.warning button:active:hover, infobar.error button:active:hover, .nautilus-window .floating-bar button:active:hover, row:selected button:checked, infobar.info button:checked, infobar.question button:checked, infobar.warning button:checked, infobar.error button:checked, .nautilus-window .floating-bar button:checked {
  color: """
            + color4
            + """;
  background-color: """
            + color1
            + """;
  border-color: """
            + color1
            + """; }

row:selected button:disabled, infobar.info button:disabled, infobar.question button:disabled, infobar.warning button:disabled, infobar.error button:disabled, .nautilus-window .floating-bar button:disabled {
  background-color: rgba(203, 204, 198, 0);
  border-color: rgba(203, 204, 198, 0.4); }
  row:selected button:disabled, infobar.info button:disabled, infobar.question button:disabled, infobar.warning button:disabled, infobar.error button:disabled, .nautilus-window .floating-bar button:disabled, row:selected button:disabled label, infobar.info button:disabled label, infobar.question button:disabled label, infobar.warning button:disabled label, infobar.error button:disabled label, .nautilus-window .floating-bar button:disabled label {
    color: rgba(203, 204, 198, 0.5); }
  .selection-mode.primary-toolbar button:disabled:active, headerbar.selection-mode button:disabled:active, .selection-mode.primary-toolbar button:disabled:checked, headerbar.selection-mode button:disabled:checked, row:selected button:disabled:active, infobar.info button:disabled:active, infobar.question button:disabled:active, infobar.warning button:disabled:active, infobar.error button:disabled:active, .nautilus-window .floating-bar button:disabled:active, .selection-mode.primary-toolbar button:disabled:checked, headerbar.selection-mode button:disabled:checked, .selection-mode.primary-toolbar button:disabled:active, headerbar.selection-mode button:disabled:active, row:selected button:disabled:checked, infobar.info button:disabled:checked, infobar.question button:disabled:checked, infobar.warning button:disabled:checked, infobar.error button:disabled:checked, .nautilus-window .floating-bar button:disabled:checked {
    color: """
            + color4
            + """;
    background-color: rgba(203, 204, 198, 0.5);
    border-color: rgba(203, 204, 198, 0.4); }

tooltip {
  border-radius: 2px;
  box-shadow: none; }
  tooltip.background {
    background-color: rgba(56, 63, 82, 0.95);
    background-clip: padding-box; }
    tooltip.background label {
      padding: 4px; }
  tooltip decoration {
    background-color: transparent; }
  tooltip * {
    background-color: transparent;
    color: """
            + color1
            + """; }

colorswatch, colorswatch:drop(active) {
  border-style: none; }

colorswatch.top {
  border-top-left-radius: 2.5px;
  border-top-right-radius: 2.5px; }
  colorswatch.top overlay {
    border-top-left-radius: 2px;
    border-top-right-radius: 2px; }

colorswatch.bottom {
  border-bottom-left-radius: 2.5px;
  border-bottom-right-radius: 2.5px; }
  colorswatch.bottom overlay {
    border-bottom-left-radius: 2px;
    border-bottom-right-radius: 2px; }

colorswatch.left, colorswatch:first-child:not(.top) {
  border-top-left-radius: 2.5px;
  border-bottom-left-radius: 2.5px; }
  colorswatch.left overlay, colorswatch:first-child:not(.top) overlay {
    border-top-left-radius: 2px;
    border-bottom-left-radius: 2px; }

colorswatch.right, colorswatch:last-child:not(.bottom) {
  border-top-right-radius: 2.5px;
  border-bottom-right-radius: 2.5px; }
  colorswatch.right overlay, colorswatch:last-child:not(.bottom) overlay {
    border-top-right-radius: 2px;
    border-bottom-right-radius: 2px; }

colorswatch.dark overlay {
  color: rgba(255, 255, 255, 0.7); }
  colorswatch.dark overlay:hover {
    border-color: #13161d; }

colorswatch.light overlay {
  color: rgba(0, 0, 0, 0.7); }
  colorswatch.light overlay:hover {
    border-color: #13161d; }

colorswatch overlay {
  border: 1px solid #13161d; }
  colorswatch overlay:hover {
    background-color: rgba(255, 255, 255, 0.2); }

colorswatch:disabled {
  opacity: 0.5; }
  colorswatch:disabled overlay {
    border-color: rgba(0, 0, 0, 0.6);
    box-shadow: none; }

colorswatch#add-color-button {
  border-style: solid;
  border-width: 1px;
  color: """
            + color1
            + """;
  border-color: #13161d;
  background-color: """
            + color5
            + """; }
  colorswatch#add-color-button:hover {
    color: """
            + color1
            + """;
    border-color: #13161d;
    background-color: #313849; }
  colorswatch#add-color-button overlay {
    border-color: transparent;
    background-color: transparent;
    background-image: none; }

button.color {
  padding: 0; }
  button.color colorswatch:first-child:last-child, button.color colorswatch:first-child:last-child overlay {
    margin: 4px;
    border-radius: 0; }

colorchooser .popover.osd {
  border-radius: 3px; }

.content-view {
  background-color: """
            + color2
            + """; }
  .content-view:hover {
    -gtk-icon-effect: highlight; }

.scale-popup button:hover {
  color: """
            + color1
            + """;
  border-color: #13161d;
  background-color: #313849; }

.context-menu, popover.touch-selection, .csd popover.touch-selection,
popover.background.touch-selection, .csd popover.background.touch-selection {
  font: initial; }

.monospace {
  font-family: Monospace; }

button.circular, button.nautilus-circular-button.image-button,
button.circular-button {
  padding: 0;
  min-width: 16px;
  min-height: 24px;
  padding: 2px 6px;
  border-radius: 50%;
  -gtk-outline-radius: 50%; }
  button.circular label, button.nautilus-circular-button.image-button label,
  button.circular-button label {
    padding: 0; }

.keycap {
  min-width: 16px;
  min-height: 20px;
  padding: 3px 6px 4px 6px;
  color: """
            + color1
            + """;
  background-color: """
            + color2
            + """;
  border: 1px solid #13161d;
  border-radius: 2.5px;
  box-shadow: inset 0px -2px 0px rgba(0, 0, 0, 0.15); }

stackswitcher button.text-button {
  min-width: 80px; }

stackswitcher button.circular, stackswitcher button.nautilus-circular-button.image-button {
  min-width: 0; }

*:drop(active):focus,
*:drop(active) {
  box-shadow: inset 0 0 0 1px #F08437; }

decoration {
  border-radius: 3px 3px 0 0;
  border-width: 0px;
  box-shadow: 0 0 0 1px rgba(17, 20, 26, 0.97), 0 8px 8px 0 rgba(0, 0, 0, 0.35);
  margin: 10px; }
  decoration:backdrop {
    box-shadow: 0 0 0 1px rgba(17, 20, 26, 0.87), 0 8px 8px 0 transparent, 0 5px 5px 0 rgba(0, 0, 0, 0.35);
    transition: 200ms ease-out; }
  .fullscreen decoration,
  .tiled decoration {
    border-radius: 0; }
  .popup decoration {
    box-shadow: none;
    border-radius: 0; }
  .ssd decoration {
    border-radius: 3px 3px 0 0;
    box-shadow: 0 0 0 1px rgba(0, 0, 0, 0.65); }
    .ssd decoration.maximized {
      border-radius: 0; }
  .csd.popup decoration {
    border-radius: 2px;
    box-shadow: 0 3px 6px rgba(0, 0, 0, 0.45), 0 0 0 1px #0b0d11; }
  tooltip.csd decoration {
    border-radius: 2px;
    box-shadow: 0 1px 3px 1px rgba(0, 0, 0, 0.25); }
  messagedialog.csd decoration {
    border-radius: 3px; }
  .solid-csd decoration {
    border-radius: 0;
    margin: 1px;
    background-color: rgba(31, 36, 48, 0.97);
    box-shadow: none; }

headerbar.default-decoration button.titlebutton,
.titlebar.default-decoration button.titlebutton {
  padding: 0 4px;
  min-width: 0;
  min-height: 0;
  margin: 0; }

headerbar button.titlebutton,
.titlebar button.titlebutton {
  padding: 0;
  min-width: 24px;
  border-color: transparent;
  background-color: transparent;
  background-image: none;
  background-color: rgba(31, 36, 48, 0); }
  headerbar button.titlebutton:hover,
  .titlebar button.titlebutton:hover {
    color: rgba(207, 209, 193, 0.8);
    border-color: rgba(7, 8, 11, 0.37);
    background-color: rgba(75, 87, 116, 0.37); }
  headerbar button.titlebutton:active, headerbar button.titlebutton:checked,
  .titlebar button.titlebutton:active,
  .titlebar button.titlebutton:checked {
    color: """
            + color1
            + """;
    border-color: transparent;
    background-color: """
            + color4
            + """; }
  headerbar button.titlebutton.close, headerbar button.titlebutton.maximize, headerbar button.titlebutton.minimize,
  .titlebar button.titlebutton.close,
  .titlebar button.titlebutton.maximize,
  .titlebar button.titlebutton.minimize {
    color: transparent;
    background-color: transparent;
    background-position: center;
    background-repeat: no-repeat;
    border-width: 0; }
    headerbar button.titlebutton.close:backdrop, headerbar button.titlebutton.maximize:backdrop, headerbar button.titlebutton.minimize:backdrop,
    .titlebar button.titlebutton.close:backdrop,
    .titlebar button.titlebutton.maximize:backdrop,
    .titlebar button.titlebutton.minimize:backdrop {
      opacity: 1; }
  headerbar button.titlebutton.close,
  .titlebar button.titlebutton.close {
    background-image: -gtk-scaled(url("assets/titlebutton-close-dark.png"), url("assets/titlebutton-close-dark@2.png")); }
  headerbar button.titlebutton.close:backdrop,
  .titlebar button.titlebutton.close:backdrop {
    background-image: -gtk-scaled(url("assets/titlebutton-close-backdrop-dark.png"), url("assets/titlebutton-close-backdrop-dark@2.png")); }
  headerbar button.titlebutton.close:hover,
  .titlebar button.titlebutton.close:hover {
    background-image: -gtk-scaled(url("assets/titlebutton-close-hover-dark.png"), url("assets/titlebutton-close-hover-dark@2.png")); }
  headerbar button.titlebutton.close:active,
  .titlebar button.titlebutton.close:active {
    background-image: -gtk-scaled(url("assets/titlebutton-close-active-dark.png"), url("assets/titlebutton-close-active-dark@2.png")); }
  headerbar button.titlebutton.maximize,
  .titlebar button.titlebutton.maximize {
    background-image: -gtk-scaled(url("assets/titlebutton-maximize-dark.png"), url("assets/titlebutton-maximize-dark@2.png")); }
  headerbar button.titlebutton.maximize:backdrop,
  .titlebar button.titlebutton.maximize:backdrop {
    background-image: -gtk-scaled(url("assets/titlebutton-maximize-backdrop-dark.png"), url("assets/titlebutton-maximize-backdrop-dark@2.png")); }
  headerbar button.titlebutton.maximize:hover,
  .titlebar button.titlebutton.maximize:hover {
    background-image: -gtk-scaled(url("assets/titlebutton-maximize-hover-dark.png"), url("assets/titlebutton-maximize-hover-dark@2.png")); }
  headerbar button.titlebutton.maximize:active,
  .titlebar button.titlebutton.maximize:active {
    background-image: -gtk-scaled(url("assets/titlebutton-maximize-active-dark.png"), url("assets/titlebutton-maximize-active-dark@2.png")); }
  headerbar button.titlebutton.minimize,
  .titlebar button.titlebutton.minimize {
    background-image: -gtk-scaled(url("assets/titlebutton-minimize-dark.png"), url("assets/titlebutton-minimize-dark@2.png")); }
  headerbar button.titlebutton.minimize:backdrop,
  .titlebar button.titlebutton.minimize:backdrop {
    background-image: -gtk-scaled(url("assets/titlebutton-minimize-backdrop-dark.png"), url("assets/titlebutton-minimize-backdrop-dark@2.png")); }
  headerbar button.titlebutton.minimize:hover,
  .titlebar button.titlebutton.minimize:hover {
    background-image: -gtk-scaled(url("assets/titlebutton-minimize-hover-dark.png"), url("assets/titlebutton-minimize-hover-dark@2.png")); }
  headerbar button.titlebutton.minimize:active,
  .titlebar button.titlebutton.minimize:active {
    background-image: -gtk-scaled(url("assets/titlebutton-minimize-active-dark.png"), url("assets/titlebutton-minimize-active-dark@2.png")); }

.view:selected, iconview:selected, .view:selected:focus, iconview:selected:focus, .view text:selected, iconview text:selected,
textview text:selected, iconview text:selected:focus,
textview text:selected:focus, .view text selection:focus, iconview text selection:focus, .view text selection, iconview text selection,
textview text selection:focus,
textview text selection, flowbox flowboxchild:selected, entry selection:focus, entry selection, menuitem.button.flat:active, menuitem.button.flat:active arrow, menuitem.button.flat:selected, menuitem.button.flat:selected arrow,
modelbutton.flat:active,
modelbutton.flat:active arrow,
modelbutton.flat:selected,
modelbutton.flat:selected arrow, treeview.view:selected, treeview.view:selected:focus, row:selected, calendar:selected, .nemo-window .nemo-window-pane widget.entry:selected:focus, .nemo-window .nemo-window-pane widget.entry:selected, filechooser placessidebar.sidebar row.sidebar-row.has-open-popup:selected, filechooser placessidebar.sidebar row.sidebar-row:selected, filechooser placessidebar.sidebar row.sidebar-row:selected:hover, filechooser placessidebar.sidebar row.sidebar-row:active:hover,
.nautilus-window placessidebar.sidebar row.sidebar-row.has-open-popup:selected,
.nautilus-window placessidebar.sidebar row.sidebar-row:selected,
.nautilus-window placessidebar.sidebar row.sidebar-row:selected:hover,
.nautilus-window placessidebar.sidebar row.sidebar-row:active:hover {
  background-color: """
            + color4
            + """; }
  row:selected label, label:selected, .view:selected, iconview:selected, .view:selected:focus, iconview:selected:focus, .view text:selected, iconview text:selected,
  textview text:selected, iconview text:selected:focus,
  textview text:selected:focus, .view text selection:focus, iconview text selection:focus, .view text selection, iconview text selection,
  textview text selection:focus,
  textview text selection, flowbox flowboxchild:selected, entry selection:focus, entry selection, menuitem.button.flat:active, menuitem.button.flat:active arrow, menuitem.button.flat:selected, menuitem.button.flat:selected arrow,
  modelbutton.flat:active,
  modelbutton.flat:active arrow,
  modelbutton.flat:selected,
  modelbutton.flat:selected arrow, treeview.view:selected, treeview.view:selected:focus, row:selected, calendar:selected, .nemo-window .nemo-window-pane widget.entry:selected:focus, .nemo-window .nemo-window-pane widget.entry:selected, filechooser placessidebar.sidebar row.sidebar-row.has-open-popup:selected, filechooser placessidebar.sidebar row.sidebar-row:selected, filechooser placessidebar.sidebar row.sidebar-row:selected:hover, filechooser placessidebar.sidebar row.sidebar-row:active:hover,
  .nautilus-window placessidebar.sidebar row.sidebar-row.has-open-popup:selected,
  .nautilus-window placessidebar.sidebar row.sidebar-row:selected,
  .nautilus-window placessidebar.sidebar row.sidebar-row:selected:hover,
  .nautilus-window placessidebar.sidebar row.sidebar-row:active:hover {
    color: """
            + color1
            + """; }
    row:selected label:disabled, label:disabled:selected, .view:disabled:selected, iconview:disabled:selected, iconview:disabled:selected:focus, .view text:disabled:selected, iconview text:disabled:selected,
    textview text:disabled:selected, iconview text selection:disabled:focus, .view text selection:disabled, iconview text selection:disabled,
    textview text selection:disabled, flowbox flowboxchild:disabled:selected, label:disabled selection, entry selection:disabled, menuitem.button.flat:disabled:active, menuitem.button.flat:active arrow:disabled, menuitem.button.flat:disabled:selected, menuitem.button.flat:selected arrow:disabled,
    modelbutton.flat:disabled:active,
    modelbutton.flat:active arrow:disabled,
    modelbutton.flat:disabled:selected,
    modelbutton.flat:selected arrow:disabled, treeview.view:disabled:selected:focus, row:disabled:selected, calendar:disabled:selected, .nemo-window .nemo-window-pane widget.entry:disabled:selected, filechooser placessidebar.sidebar row.sidebar-row:disabled:selected, filechooser placessidebar.sidebar row.sidebar-row:disabled:active:hover,
    .nautilus-window placessidebar.sidebar row.sidebar-row:disabled:selected,
    .nautilus-window placessidebar.sidebar row.sidebar-row:disabled:active:hover {
      color: #808990; }

.gedit-bottom-panel-paned notebook > header.top > tabs > tab:checked,
terminal-window notebook > header.top > tabs > tab:checked {
  box-shadow: inset 0 -1px #13161d; }

terminal-window notebook > header.top,
.mate-terminal notebook > header.top {
  padding-top: 3px;
  box-shadow: inset 0 1px #171b24, inset 0 -1px #13161d; }
  terminal-window notebook > header.top button,
  .mate-terminal notebook > header.top button {
    padding: 0;
    min-width: 24px;
    min-height: 24px; }

.nautilus-canvas-item {
  border-radius: 2px; }

.nautilus-desktop.nautilus-canvas-item, .nemo-desktop.nemo-canvas-item, .caja-desktop {
  color: white;
  text-shadow: 1px 1px rgba(0, 0, 0, 0.6); }
  .nautilus-desktop.nautilus-canvas-item:active, .nemo-desktop.nemo-canvas-item:active, .caja-desktop:active {
    color: """
            + color1
            + """; }
  .nautilus-desktop.nautilus-canvas-item:selected, .nemo-desktop.nemo-canvas-item:selected, .caja-desktop:selected {
    color: """
            + color1
            + """;
    text-shadow: none; }

.nautilus-canvas-item.dim-label, label.nautilus-canvas-item.separator,
popover.background label.nautilus-canvas-item.separator, headerbar .nautilus-canvas-item.subtitle, .titlebar:not(headerbar) .nautilus-canvas-item.subtitle,
.nautilus-list-dim-label {
  color: #75787b; }
  .nautilus-canvas-item.dim-label:selected, label.nautilus-canvas-item.separator:selected, headerbar .nautilus-canvas-item.subtitle:selected, .titlebar:not(headerbar) .nautilus-canvas-item.subtitle:selected, .nautilus-canvas-item.dim-label:selected:focus, label.nautilus-canvas-item.separator:selected:focus, headerbar .nautilus-canvas-item.subtitle:selected:focus, .titlebar:not(headerbar) .nautilus-canvas-item.subtitle:selected:focus,
  .nautilus-list-dim-label:selected,
  .nautilus-list-dim-label:selected:focus {
    color: #adb1b0; }

.nautilus-window searchbar {
  border-top: 1px solid #13161d; }

.nautilus-window .searchbar-container {
  margin-top: -1px; }

.nautilus-window notebook,
.nautilus-window notebook > stack:not(:only-child) searchbar {
  background-color: """
            + color2
            + """; }

.disk-space-display {
  border-style: solid;
  border-width: 1px; }
  .disk-space-display.unknown {
    background-color: rgba(203, 204, 198, 0.5);
    border-color: rgba(178, 180, 171, 0.5); }
  .disk-space-display.used {
    background-color: rgba(52, 69, 90, 0.8);
    border-color: rgba(33, 44, 58, 0.8); }
  .disk-space-display.free {
    background-color: """
            + color6
            + """;
    border-color: #050608; }

@keyframes needs_attention_keyframes {
  0% {
    color: rgba(207, 209, 193, 0.8);
    border-color: rgba(7, 8, 11, 0.37);
    background-color: rgba(75, 87, 116, 0.37); }
  100% {
    color: """
            + color1
            + """;
    border-color: transparent;
    background-color: """
            + color4
            + """; } }

.nautilus-operations-button-needs-attention {
  animation: needs_attention_keyframes 2s ease-in-out; }

.nautilus-operations-button-needs-attention-multiple {
  animation: needs_attention_keyframes 3s ease-in-out;
  animation-iteration-count: 3; }

.conflict-row.activatable, .conflict-row.activatable:active {
  color: white;
  background-color: #FC4138; }

.conflict-row.activatable:hover {
  background-color: #fd716a; }

.conflict-row.activatable:selected {
  color: """
            + color1
            + """;
  background-color: """
            + color4
            + """; }

.nemo-window .nemo-places-sidebar.frame {
  border-width: 0; }

.nemo-window notebook {
  background-color: """
            + color2
            + """; }

.nemo-window .nemo-window-pane widget.entry {
  border: 1px solid;
  border-radius: 3px;
  color: """
            + color1
            + """;
  border-color: #13161d;
  background-color: """
            + color2
            + """;
  box-shadow: inset 1px 0 """
            + color4
            + """, inset -1px 0 """
            + color4
            + """, inset 0 1px """
            + color4
            + """, inset 0 -1px """
            + color4
            + """; }

.nemo-window .primary-toolbar widget.raised.linked:not(.vertical):not(.path-bar) > button {
  color: rgba(207, 209, 193, 0.8);
  border-color: rgba(7, 8, 11, 0.37);
  background-color: rgba(75, 87, 116, 0.37); }
  .nemo-window .primary-toolbar widget.raised.linked:not(.vertical):not(.path-bar) > button:not(:last-child):not(:only-child) {
    margin: 0 0 1px 0; }
  .nemo-window .primary-toolbar widget.raised.linked:not(.vertical):not(.path-bar) > button:hover {
    background-color: rgba(108, 123, 160, 0.37); }
  .nemo-window .primary-toolbar widget.raised.linked:not(.vertical):not(.path-bar) > button:active, .nemo-window .primary-toolbar widget.raised.linked:not(.vertical):not(.path-bar) > button:checked {
    color: """
            + color1
            + """;
    border-color: transparent;
    background-color: """
            + color4
            + """; }
  .nemo-window .primary-toolbar widget.raised.linked:not(.vertical):not(.path-bar) > button:disabled {
    color: rgba(207, 209, 193, 0.4); }

.nemo-window .primary-toolbar widget.raised.linked:not(.vertical):not(.path-bar) > button + button {
  border-left-style: none; }

.nemo-window .primary-toolbar widget.raised.linked:not(.vertical):not(.path-bar) > button:hover:not(:checked):not(:active):not(:only-child):hover {
  box-shadow: inset 1px 0 rgba(7, 8, 11, 0.37), inset -1px 0 rgba(7, 8, 11, 0.37); }

.nemo-window .primary-toolbar widget.raised.linked:not(.vertical):not(.path-bar) > button:hover:not(:checked):not(:active):not(:only-child):first-child:hover {
  box-shadow: inset -1px 0 rgba(7, 8, 11, 0.37); }

.nemo-window .primary-toolbar widget.raised.linked:not(.vertical):not(.path-bar) > button:hover:not(:checked):not(:active):not(:only-child):last-child:hover {
  box-shadow: inset 1px 0 rgba(7, 8, 11, 0.37); }

.caja-notebook {
  border-top: 1px solid #13161d; }

.caja-side-pane .frame {
  border-width: 1px 0 0; }

.caja-notebook .frame {
  border-width: 0 0 1px; }

.open-document-selector-treeview.view, iconview.open-document-selector-treeview {
  padding: 3px 6px 3px 6px;
  border-color: """
            + color2
            + """; }
  .open-document-selector-treeview.view:hover, iconview.open-document-selector-treeview:hover {
    background-color: #2f333e; }
    .open-document-selector-treeview.view:hover:selected, iconview.open-document-selector-treeview:hover:selected {
      color: """
            + color1
            + """;
      background-color: """
            + color4
            + """; }

.open-document-selector-name-label {
  color: """
            + color1
            + """; }

.open-document-selector-path-label {
  color: #777a7d;
  font-size: smaller; }
  .open-document-selector-path-label:selected {
    color: rgba(203, 204, 198, 0.9); }

.gedit-document-panel row button {
  min-width: 22px;
  min-height: 22px;
  padding: 0;
  color: transparent;
  background: none;
  border: none;
  box-shadow: none; }
  .gedit-document-panel row button image {
    color: inherit; }

.gedit-document-panel row:hover:not(:selected) button {
  color: #8f9192; }
  .gedit-document-panel row:hover:not(:selected) button:hover {
    color: #ff4d4d; }
  .gedit-document-panel row:hover:not(:selected) button:active {
    color: """
            + color1
            + """; }

.gedit-document-panel row:hover:selected button:hover {
  color: #ff6666;
  background: none;
  border: none;
  box-shadow: none; }
  .gedit-document-panel row:hover:selected button:hover:active {
    color: """
            + color1
            + """; }

.gedit-document-panel-dragged-row {
  border: 1px solid #13161d;
  background-color: #0b0d11;
  color: """
            + color1
            + """; }

.gedit-side-panel-paned statusbar {
  border-top: 1px solid #13161d;
  background-color: """
            + color6
            + """; }

.gedit-search-slider {
  background-color: #232936;
  padding: 6px;
  border-color: #13161d;
  border-radius: 0 0 2px 2px;
  border-width: 0 1px 1px 1px;
  border-style: solid; }

.gedit-search-entry-occurrences-tag {
  color: rgba(203, 204, 198, 0.6);
  border: none;
  margin: 2px;
  padding: 2px; }

.gedit-map-frame border {
  border-width: 0; }
  .gedit-map-frame border:dir(ltr) {
    border-left-width: 1px; }
  .gedit-map-frame border:dir(rtl) {
    border-right-width: 1px; }

.pluma-window statusbar frame > border {
  border: none; }

.pluma-window notebook > stack scrolledwindow {
  border-width: 0 0 1px 0; }

#pluma-status-combo-button {
  min-height: 0;
  padding: 0;
  border-top: none;
  border-bottom: none;
  border-radius: 0; }

.gb-search-entry-occurrences-tag {
  background: none; }

workbench.csd > stack.titlebar:not(headerbar) {
  padding: 0;
  background: none;
  border: none;
  box-shadow: none; }
  workbench.csd > stack.titlebar:not(headerbar) headerbar, workbench.csd > stack.titlebar:not(headerbar) headerbar:first-child, workbench.csd > stack.titlebar:not(headerbar) headerbar:last-child {
    border-radius: 3px 3px 0 0; }

editortweak .linked > entry.search:focus + .gb-linked-scroller {
  border-top-color: """
            + color4
            + """; }

layouttab {
  background-color: """
            + color2
            + """; }

layout {
  border: 1px solid #13161d;
  -PnlDockBin-handle-size: 1; }

eggsearchbar box.search-bar {
  border-bottom: 1px solid #13161d; }

pillbox {
  color: """
            + color1
            + """;
  background-color: """
            + color4
            + """;
  border-radius: 3px; }
  pillbox:disabled label {
    color: rgba(203, 204, 198, 0.5); }

docktabstrip {
  padding: 0 6px;
  background-color: """
            + color6
            + """;
  border-bottom: 1px solid #13161d; }
  docktabstrip docktab {
    min-height: 28px;
    border: solid transparent;
    border-width: 0 1px; }
    docktabstrip docktab label {
      opacity: 0.5; }
    docktabstrip docktab:checked label, docktabstrip docktab:hover label {
      opacity: 1; }
    docktabstrip docktab:checked {
      border-color: #13161d;
      background-color: """
            + color2
            + """; }

dockbin {
  border: 1px solid #13161d;
  -PnlDockBin-handle-size: 1; }

dockpaned {
  border: 1px solid #13161d; }

dockoverlayedge {
  background-color: """
            + color6
            + """; }
  dockoverlayedge docktabstrip {
    padding: 0;
    border: none; }
  dockoverlayedge.left-edge tab:checked,
  dockoverlayedge.right-edge tab:checked {
    border-width: 1px 0; }

popover.messagepopover.background {
  padding: 0; }

popover.messagepopover .popover-content-area {
  margin: 16px; }

popover.messagepopover .popover-action-area {
  margin: 8px; }
  popover.messagepopover .popover-action-area button:not(:first-child):not(:last-child) {
    margin: 0 4px; }

popover.popover-selector {
  padding: 0; }
  popover.popover-selector list row {
    padding: 5px 0; }
  popover.popover-selector list row image {
    margin-left: 3px;
    margin-right: 10px; }

entry.search.preferences-search {
  border: none;
  border-right: 1px solid #13161d;
  border-bottom: 1px solid #13161d;
  border-radius: 0; }

preferences stacksidebar.sidebar list {
  background-image: linear-gradient(to bottom, """
            + color2
            + """, """
            + color2
            + """); }

preferences stacksidebar.sidebar list separator {
  background-color: transparent; }

devhelppanel entry:focus,
symboltreepanel entry:focus {
  border-color: #13161d; }

button.run-arrow-button {
  min-width: 12px; }

omnibar.linked > entry:not(:only-child) {
  border-style: solid;
  border-radius: 3px;
  margin-left: 1px;
  margin-right: 1px; }

gstyleslidein #scale_box button.toggle:checked,
gstyleslidein #strings_controls button.toggle:checked,
gstyleslidein #palette_controls button.toggle:checked,
gstyleslidein #components_controls button.toggle:checked {
  color: """
            + color1
            + """; }

configurationview entry.flat {
  background: none; }

configurationview list {
  border-width: 0; }

.documents-scrolledwin.frame {
  border-width: 0; }

button.documents-load-more {
  border-width: 1px 0 0;
  border-radius: 0; }

.documents-icon-bg {
  background-color: """
            + color4
            + """;
  color: """
            + color1
            + """;
  border-radius: 2px; }

.documents-collection-icon, .photos-collection-icon {
  background-color: rgba(203, 204, 198, 0.3);
  border-radius: 2px; }

button.documents-favorite:active,
button.documents-favorite:active:hover {
  color: #59779b; }

.documents-entry-tag, .photos-entry-tag {
  color: """
            + color1
            + """;
  background: """
            + color4
            + """;
  border-radius: 2px;
  border-width: 0;
  margin: 2px;
  padding: 4px; }
  .documents-entry-tag:hover, .photos-entry-tag:hover {
    color: """
            + color1
            + """;
    background: #3b4f67; }
  .documents-entry-tag:active, .photos-entry-tag:active {
    color: """
            + color1
            + """;
    background: #2d3b4d; }

.content-view.document-page {
  border-style: solid;
  border-width: 3px 3px 6px 4px;
  border-image: url("assets/thumbnail-frame.png") 3 3 6 4; }

.photos-fade-in {
  opacity: 1.0;
  transition: opacity 0.2s ease-out; }

.photos-fade-out {
  opacity: 0.0;
  transition: opacity 0.2s ease-out; }

.tweak-categories,
.tweak-category:not(:selected):not(:hover) {
  background-image: linear-gradient(to bottom, """
            + color2
            + """, """
            + color2
            + """); }

.tr-workarea undershoot,
.tr-workarea overshoot {
  border-color: transparent; }

.atril-window .primary-toolbar toolbar, .atril-window .primary-toolbar .inline-toolbar {
  background: none; }

#gf-bubble, #gf-bubble.solid,
#gf-osd-window,
#gf-osd-window.solid,
#gf-input-source-popup,
#gf-input-source-popup.solid,
#gf-candidate-popup,
#gf-candidate-popup.solid {
  color: #dcddd9;
  background-color: rgba(35, 40, 52, 0.95);
  border: 1px solid rgba(19, 21, 28, 0.95);
  border-radius: 2px; }

#gf-bubble levelbar block.low, #gf-bubble levelbar block.high, #gf-bubble levelbar block.full,
#gf-osd-window levelbar block.low,
#gf-osd-window levelbar block.high,
#gf-osd-window levelbar block.full,
#gf-input-source-popup levelbar block.low,
#gf-input-source-popup levelbar block.high,
#gf-input-source-popup levelbar block.full,
#gf-candidate-popup levelbar block.low,
#gf-candidate-popup levelbar block.high,
#gf-candidate-popup levelbar block.full {
  background-color: """
            + color4
            + """;
  border-color: """
            + color4
            + """; }

#gf-bubble levelbar block.empty,
#gf-osd-window levelbar block.empty,
#gf-input-source-popup levelbar block.empty,
#gf-candidate-popup levelbar block.empty {
  background-color: rgba(25, 28, 37, 0.95); }

#gf-bubble levelbar trough,
#gf-osd-window levelbar trough,
#gf-input-source-popup levelbar trough,
#gf-candidate-popup levelbar trough {
  background: none; }

#gf-input-source {
  min-height: 32px;
  min-width: 40px; }
  #gf-input-source:selected {
    color: """
            + color1
            + """;
    background-color: """
            + color4
            + """;
    border-radius: 2px; }

gf-candidate-box label {
  padding: 3px; }

gf-candidate-box:hover, gf-candidate-box:selected {
  color: """
            + color1
            + """;
  background-color: """
            + color4
            + """;
  border-radius: 2px; }

MsdOsdWindow.background.osd {
  border-radius: 2px;
  border: 1px solid rgba(19, 21, 28, 0.95); }
  MsdOsdWindow.background.osd .progressbar {
    background-color: """
            + color4
            + """;
    border: none;
    border-color: red;
    border-radius: 5px; }
  MsdOsdWindow.background.osd .trough {
    background-color: rgba(25, 28, 37, 0.95);
    border: none;
    border-radius: 5px; }

.mate-panel-menu-bar, .mate-panel-menu-bar menubar,
panel-toplevel.background,
panel-toplevel.background menubar {
  background-color: #191d26; }

.mate-panel-menu-bar menubar,
.mate-panel-menu-bar #PanelApplet label,
.mate-panel-menu-bar #PanelApplet image,
panel-toplevel.background menubar,
panel-toplevel.background #PanelApplet label,
panel-toplevel.background #PanelApplet image {
  color: """
            + color1
            + """; }

.mate-panel-menu-bar button label, .mate-panel-menu-bar button image,
.mate-panel-menu-bar #tasklist-button label,
.mate-panel-menu-bar #tasklist-button image,
panel-toplevel.background button label,
panel-toplevel.background button image,
panel-toplevel.background #tasklist-button label,
panel-toplevel.background #tasklist-button image {
  color: inherit; }

.mate-panel-menu-bar .wnck-pager,
panel-toplevel.background .wnck-pager {
  color: #666663;
  background-color: rgba(5, 6, 7, 0.95); }
  .mate-panel-menu-bar .wnck-pager:hover,
  panel-toplevel.background .wnck-pager:hover {
    background-color: rgba(36, 41, 53, 0.95); }
  .mate-panel-menu-bar .wnck-pager:selected,
  panel-toplevel.background .wnck-pager:selected {
    color: #59779b;
    background-color: """
            + color4
            + """; }

.mate-panel-menu-bar na-tray-applet,
panel-toplevel.background na-tray-applet {
  -NaTrayApplet-icon-padding: 0;
  -NaTrayApplet-icon-size: 16px; }

.xfce4-panel.panel {
  background-color: rgba(25, 29, 38, 0.95);
  text-shadow: none;
  -gtk-icon-shadow: none; }

#tasklist-button {
  color: rgba(203, 204, 198, 0.8);
  border-radius: 0;
  border: none;
  background-color: rgba(25, 29, 38, 0); }
  #tasklist-button:hover {
    color: #e4e4e1;
    background-color: rgba(0, 0, 0, 0.17); }
  #tasklist-button:checked {
    color: white;
    background-color: rgba(0, 0, 0, 0.25);
    box-shadow: inset 0 -2px """
            + color4
            + """; }

.mate-panel-menu-bar button:not(#tasklist-button),
panel-toplevel.background button:not(#tasklist-button), .xfce4-panel.panel button.flat, .xfce4-panel.panel button.sidebar-button {
  color: """
            + color1
            + """;
  border-radius: 0;
  border: none;
  background-color: rgba(25, 29, 38, 0); }
  .mate-panel-menu-bar button:hover:not(#tasklist-button),
  panel-toplevel.background button:hover:not(#tasklist-button), .xfce4-panel.panel button.flat:hover, .xfce4-panel.panel button.sidebar-button:hover {
    border: none;
    background-color: rgba(46, 52, 68, 0.95); }
  .mate-panel-menu-bar button:active:not(#tasklist-button),
  panel-toplevel.background button:active:not(#tasklist-button), .xfce4-panel.panel button.flat:active, .xfce4-panel.panel button.sidebar-button:active, .mate-panel-menu-bar button:checked:not(#tasklist-button),
  panel-toplevel.background button:checked:not(#tasklist-button), .xfce4-panel.panel button.flat:checked, .xfce4-panel.panel button.sidebar-button:checked {
    color: """
            + color1
            + """;
    border: none;
    background-color: """
            + color4
            + """; }
    .mate-panel-menu-bar button:active:not(#tasklist-button) label,
    panel-toplevel.background button:active:not(#tasklist-button) label, .xfce4-panel.panel button.flat:active label, .xfce4-panel.panel button.sidebar-button:active label, .mate-panel-menu-bar button:active:not(#tasklist-button) image,
    panel-toplevel.background button:active:not(#tasklist-button) image, .xfce4-panel.panel button.flat:active image, .xfce4-panel.panel button.sidebar-button:active image, .mate-panel-menu-bar button:checked:not(#tasklist-button) label,
    panel-toplevel.background button:checked:not(#tasklist-button) label, .xfce4-panel.panel button.flat:checked label, .xfce4-panel.panel button.sidebar-button:checked label, .mate-panel-menu-bar button:checked:not(#tasklist-button) image,
    panel-toplevel.background button:checked:not(#tasklist-button) image, .xfce4-panel.panel button.flat:checked image, .xfce4-panel.panel button.sidebar-button:checked image {
      color: inherit; }

.nautilus-window .floating-bar {
  padding: 1px;
  background-color: """
            + color4
            + """;
  color: """
            + color1
            + """;
  border-radius: 2px 2px 0 0; }
  .nautilus-window .floating-bar.bottom.left {
    border-top-left-radius: 0; }
  .nautilus-window .floating-bar.bottom.right {
    border-top-right-radius: 0; }
  .nautilus-window .floating-bar button {
    border: none;
    border-radius: 0;
    min-height: 0; }

.marlin-pathbar.pathbar {
  border-radius: 3px;
  padding-left: 4px;
  padding-right: 4px;
  color: rgba(207, 209, 193, 0.8);
  border-color: rgba(7, 8, 11, 0.37);
  background-color: rgba(75, 87, 116, 0.37); }
  .marlin-pathbar.pathbar image, .marlin-pathbar.pathbar image:hover {
    color: inherit; }
  .marlin-pathbar.pathbar:focus {
    color: """
            + color1
            + """;
    border-color: transparent;
    background-color: """
            + color4
            + """; }
  .marlin-pathbar.pathbar:disabled {
    color: rgba(207, 209, 193, 0.35);
    border-color: rgba(7, 8, 11, 0.37);
    background-color: rgba(75, 87, 116, 0.22); }
  .marlin-pathbar.pathbar:active, .marlin-pathbar.pathbar:checked {
    color: """
            + color4
            + """; }

.gala-notification {
  border: 1px solid rgba(0, 0, 0, 0.35);
  border-radius: 3px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
  background-image: linear-gradient(to bottom, white, white);
  background-color: transparent; }
  .gala-notification .title, .gala-notification .label {
    color: #5c616c; }

.panel {
  background-color: transparent;
  color: white;
  font-weight: bold;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.6);
  -gtk-icon-shadow: 0 1px 2px rgba(0, 0, 0, 0.6); }
  .panel-shadow {
    background-image: none;
    background-color: transparent; }
  .panel .menu {
    box-shadow: none; }
    .panel .menu .menuitem {
      font-weight: normal;
      text-shadow: none;
      -gtk-icon-shadow: none; }
    .panel .menu .window-frame.menu.csd,
    .panel .menu .window-frame.popup.csd {
      box-shadow: 0 0 0 1px rgba(0, 0, 0, 0.2), 0 10px 20px rgba(0, 0, 0, 0.19), 0 6px 6px rgba(0, 0, 0, 0.23); }
  .panel .menubar > .menuitem {
    padding: 3px 6px; }
    .panel .menubar > .menuitem:hover {
      background-color: transparent; }
  .panel .window-frame.menu.csd,
  .panel .window-frame.popup.csd {
    box-shadow: none; }

.composited-indicator {
  background-color: transparent;
  color: white;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.6);
  -gtk-icon-shadow: 0 1px 2px rgba(0, 0, 0, 0.6); }
  .composited-indicator > GtkWidget > GtkWidget:first-child {
    padding: 0 2px; }
  .composited-indicator .menuitem:active, .composited-indicator .menuitem:hover {
    border-style: none;
    background-image: none;
    box-shadow: none; }
  .composited-indicator > .popup > .menu {
    padding-top: 8px;
    padding-bottom: 8px; }

.panel-app-button > GtkWidget > GtkWidget:first-child {
  padding: 0 2px 0 4px; }

.panel .menu .spinner,
.menu .spinner {
  opacity: 1; }

UnityDecoration {
  -UnityDecoration-extents: 28px 1 1 1;
  -UnityDecoration-input-extents: 10px;
  -UnityDecoration-shadow-offset-x: 0px;
  -UnityDecoration-shadow-offset-y: 3px;
  -UnityDecoration-active-shadow-color: rgba(0, 0, 0, 0.2);
  -UnityDecoration-active-shadow-radius: 12px;
  -UnityDecoration-inactive-shadow-color: rgba(0, 0, 0, 0.07);
  -UnityDecoration-inactive-shadow-radius: 7px;
  -UnityDecoration-glow-size: 10px;
  -UnityDecoration-glow-color: """
            + color4
            + """;
  -UnityDecoration-title-indent: 10px;
  -UnityDecoration-title-fade: 35px;
  -UnityDecoration-title-alignment: 0.0; }
  UnityDecoration .top {
    border: 1px solid rgba(17, 20, 26, 0.97);
    border-bottom-width: 0;
    border-radius: 4px 4px 0 0;
    padding: 1px 6px 0 6px;
    background-image: linear-gradient(to bottom, """
            + color6
            + """, """
            + color6
            + """);
    color: rgba(207, 209, 193, 0.8);
    box-shadow: inset 0 1px rgba(37, 43, 57, 0.97); }
    UnityDecoration .top:backdrop {
      border-bottom-width: 0;
      color: rgba(207, 209, 193, 0.5); }
  UnityDecoration .left, UnityDecoration .right, UnityDecoration .bottom,
  UnityDecoration .left:backdrop, UnityDecoration .right:backdrop, UnityDecoration .bottom:backdrop {
    background-color: transparent;
    background-image: linear-gradient(to bottom, rgba(17, 20, 26, 0.97), rgba(17, 20, 26, 0.97)); }

UnityPanelWidget,
.unity-panel {
  background-image: linear-gradient(to bottom, #2f343f, #2f343f);
  color: #fcfcfc;
  box-shadow: none; }
  UnityPanelWidget:backdrop,
  .unity-panel:backdrop {
    color: #cdcec9; }

.unity-panel.menubar.menuitem:hover,
.unity-panel.menubar .menuitem *:hover {
  border-radius: 0;
  color: """
            + color1
            + """;
  background-image: linear-gradient(to bottom, """
            + color4
            + """, """
            + color4
            + """);
  border-bottom: none; }

.lightdm.menu {
  background-image: none;
  background-color: rgba(0, 0, 0, 0.4);
  border-color: rgba(255, 255, 255, 0.8);
  border-radius: 4px;
  padding: 1px;
  color: white; }

.lightdm-combo .menu {
  background-color: rgba(47, 55, 73, 0.97);
  border-radius: 0px;
  padding: 0px;
  color: white; }

.lightdm.menu .menuitem *,
.lightdm.menu .menuitem.check:active,
.lightdm.menu .menuitem.radio:active {
  color: white; }

.lightdm.menubar {
  color: rgba(255, 255, 255, 0.8);
  background-image: none;
  background-color: rgba(0, 0, 0, 0.5); }
  .lightdm.menubar > .menuitem {
    padding: 2px 6px; }

.lightdm-combo.combobox-entry .button,
.lightdm-combo .cell,
.lightdm-combo .button,
.lightdm-combo .entry,
.lightdm.button,
.lightdm.entry {
  background-image: none;
  background-color: rgba(0, 0, 0, 0.3);
  border-color: rgba(255, 255, 255, 0.4);
  border-radius: 10px;
  padding: 7px;
  color: white;
  text-shadow: none; }

.lightdm.button,
.lightdm.button:hover,
.lightdm.button:active,
.lightdm.button:active:focus,
.lightdm.entry,
.lightdm.entry:hover,
.lightdm.entry:active,
.lightdm.entry:active:focus {
  background-image: none;
  border-image: none; }

.lightdm.button:focus,
.lightdm.entry:focus {
  border-color: rgba(255, 255, 255, 0.1);
  border-width: 1px;
  border-style: solid;
  color: white; }

.lightdm.entry:selected {
  background-color: rgba(255, 255, 255, 0.8); }

.lightdm.entry:active {
  -gtk-icon-source: -gtk-icontheme("process-working-symbolic");
  animation: dashentry_spinner 1s infinite linear; }

.lightdm.option-button {
  padding: 2px;
  background: none;
  border: 0; }

.lightdm.toggle-button {
  background: none;
  border-width: 0; }
  .lightdm.toggle-button.selected {
    background-color: rgba(0, 0, 0, 0.7);
    border-width: 1px; }

@keyframes dashentry_spinner {
  to {
    -gtk-icon-transform: rotate(1turn); } }

.overlay-bar {
  background-color: """
            + color4
            + """;
  border-color: """
            + color4
            + """;
  border-radius: 2px;
  padding: 3px 6px;
  margin: 3px; }
  .overlay-bar label {
    color: """
            + color1
            + """; }

GraniteWidgetsThinPaned {
  background-color: transparent;
  background-image: none;
  margin: 0;
  border-left: 1px solid #13161d;
  border-right: 1px solid #13161d; }

GraniteWidgetsPopOver .frame,
GraniteWidgetsStaticNotebook .frame {
  border: none; }

.help_button {
  border-radius: 100px;
  padding: 3px 9px; }

toolbar.secondary-toolbar, .secondary-toolbar.inline-toolbar {
  padding: 3px;
  border-bottom: 1px solid #13161d; }
  toolbar.secondary-toolbar button, .secondary-toolbar.inline-toolbar button {
    padding: 0 3px 0 3px; }

toolbar.bottom-toolbar, .bottom-toolbar.inline-toolbar {
  padding: 5px;
  border-width: 1px 0 0 0;
  border-style: solid;
  border-color: #13161d;
  background-color: """
            + color6
            + """; }
  toolbar.bottom-toolbar button, .bottom-toolbar.inline-toolbar button {
    padding: 2px 3px 2px 3px; }

.source-list {
  -GtkTreeView-horizontal-separator: 1px;
  -GtkTreeView-vertical-separator: 6px; }

.source-list,
.source-list.view,
iconview.source-list {
  background-color: """
            + color6
            + """;
  color: """
            + color1
            + """;
  -gtk-icon-style: regular; }

.source-list.category-expander {
  color: transparent; }

.source-list.view:hover, iconview.source-list:hover {
  background-color: #29303f; }

.source-list.view:selected, iconview.source-list:selected,
.source-list.view:hover:selected,
iconview.source-list:hover:selected,
.source-list.view:selected:focus,
iconview.source-list:selected:focus,
.source-list.category-expander:hover {
  color: """
            + color1
            + """;
  background-color: """
            + color4
            + """; }

.source-list scrollbar,
.source-list junction {
  border-image: none;
  border-color: transparent;
  background-color: """
            + color6
            + """;
  background-image: none; }

.source-list.badge,
.source-list.badge:hover,
.source-list.badge:selected,
.source-list.badge:selected:focus,
.source-list.badge:hover:selected {
  background-image: none;
  background-color: """
            + color4
            + """;
  color: """
            + color1
            + """;
  border-radius: 10px;
  padding: 0 6px;
  margin: 0 3px;
  border-width: 0; }

.source-list.badge:selected,
.source-list.badge:selected:focus,
.source-list.badge:hover:selected {
  background-color: """
            + color1
            + """;
  color: """
            + color4
            + """; }

.source-list.category-expander {
  color: """
            + color1
            + """;
  -gtk-icon-source: -gtk-icontheme("pan-end-symbolic");
  -GtkTreeView-expander-size: 16; }

.source-list.category-expander,
.source-list.category-expander:backdrop {
  color: transparent;
  border: none; }

.source-list.category-expander:checked {
  -gtk-icon-source: -gtk-icontheme("pan-down-symbolic"); }

GraniteWidgetsWelcome {
  background-color: """
            + color2
            + """; }

GraniteWidgetsWelcome label {
  color: #75787b;
  font-size: 11px;
  text-shadow: none; }

GraniteWidgetsWelcome .h1,
GraniteWidgetsWelcome .h3 {
  color: rgba(203, 204, 198, 0.8); }

.help_button {
  border-radius: 0; }

GraniteWidgetsPopOver {
  -GraniteWidgetsPopOver-arrow-width: 21;
  -GraniteWidgetsPopOver-arrow-height: 10;
  -GraniteWidgetsPopOver-border-radius: 2px;
  -GraniteWidgetsPopOver-border-width: 1;
  -GraniteWidgetsPopOver-shadow-size: 12;
  border: 1px solid rgba(0, 0, 0, 0.3);
  margin: 0; }

.popover_bg {
  background-image: linear-gradient(to bottom, """
            + color2
            + """, """
            + color2
            + """);
  border: 1px solid rgba(0, 0, 0, 0.3); }

GraniteWidgetsPopOver .sidebar.view, GraniteWidgetsPopOver iconview.sidebar,
GraniteWidgetsPopOver * {
  background-color: transparent; }

GraniteWidgetsXsEntry entry {
  padding: 4px; }

.h1 {
  font-size: 24px; }

.h2 {
  font-size: 18px; }

.h3 {
  font-size: 11px; }

.h4,
.category-label {
  color: #979a99;
  font-weight: 600; }

.h4 {
  padding-bottom: 6px;
  padding-top: 6px; }

GtkListBox .h4 {
  padding-left: 6px; }

#panel_window {
  background-color: rgba(25, 29, 38, 0.95);
  color: """
            + color1
            + """;
  font-weight: bold;
  box-shadow: inset 0 -1px rgba(11, 13, 16, 0.95); }
  #panel_window menubar {
    padding-left: 5px; }
    #panel_window menubar, #panel_window menubar > menuitem {
      background-color: transparent;
      color: """
            + color1
            + """;
      font-weight: bold; }
  #panel_window menubar menuitem:disabled {
    color: rgba(203, 204, 198, 0.5); }
    #panel_window menubar menuitem:disabled label {
      color: inherit; }
  #panel_window menubar menu > menuitem {
    font-weight: normal; }

#login_window,
#shutdown_dialog,
#restart_dialog {
  font-weight: normal;
  border-style: none;
  background-color: transparent;
  color: """
            + color1
            + """; }

#content_frame {
  padding-bottom: 14px;
  background-color: """
            + color6
            + """;
  border-top-left-radius: 2px;
  border-top-right-radius: 2px;
  border: solid rgba(0, 0, 0, 0.1);
  border-width: 1px 1px 0 1px; }

#content_frame button {
  color: """
            + color1
            + """;
  border-color: #13161d;
  background-color: """
            + color5
            + """; }
  #content_frame button:hover {
    color: """
            + color1
            + """;
    border-color: #13161d;
    background-color: #313849; }
  #content_frame button:active, #content_frame button:checked {
    color: """
            + color1
            + """;
    border-color: #13161d;
    background-color: """
            + color4
            + """; }
  #content_frame button:disabled {
    border-color: rgba(19, 22, 29, 0.55);
    background-color: rgba(39, 45, 58, 0.55); }
    #content_frame button:disabled label, #content_frame button:disabled {
      color: rgba(203, 204, 198, 0.45); }

#buttonbox_frame {
  padding-top: 20px;
  padding-bottom: 0px;
  border-style: none;
  background-color: rgba(31, 36, 48, 0.97);
  border-bottom-left-radius: 3px;
  border-bottom-right-radius: 3px;
  border: solid rgba(0, 0, 0, 0.1);
  border-width: 0 1px 1px 1px;
  box-shadow: inset 0 1px rgba(23, 27, 36, 0.97); }

#buttonbox_frame button {
  color: """
            + color1
            + """;
  border-color: rgba(10, 12, 15, 0.35);
  background-color: rgba(80, 92, 119, 0.35); }
  #buttonbox_frame button:hover {
    color: """
            + color1
            + """;
    border-color: rgba(10, 12, 15, 0.35);
    background-color: rgba(95, 108, 140, 0.45); }
  #buttonbox_frame button:active, #buttonbox_frame button:checked {
    color: """
            + color1
            + """;
    border-color: rgba(10, 12, 15, 0.35);
    background-color: """
            + color4
            + """; }
  #buttonbox_frame button:disabled {
    color: #555960;
    border-color: rgba(10, 12, 15, 0.35);
    background-color: rgba(80, 92, 119, 0.2); }

#login_window #user_combobox {
  color: """
            + color1
            + """;
  font-size: 13px; }
  #login_window #user_combobox menu {
    font-weight: normal; }

#user_image {
  padding: 3px;
  border-radius: 2px; }

#shutdown_button.button {
  background-clip: border-box;
  color: green;
  background-color: #F04A50;
  border-color: #F04A50; }
  #shutdown_button.button:hover {
    background-clip: border-box;
    color: green;
    background-color: #f4797e;
    border-color: #f4797e; }
  #shutdown_button.button:active, #shutdown_button.button:checked {
    background-clip: border-box;
    color: green;
    background-color: #ec1b22;
    border-color: #ec1b22; }

#restart_button.button {
  background-clip: border-box;
  color: green;
  background-color: #4DADD4;
  border-color: #4DADD4; }
  #restart_button.button:hover {
    background-clip: border-box;
    color: green;
    background-color: #76c0de;
    border-color: #76c0de; }
  #restart_button.button:active, #restart_button.button:checked {
    background-clip: border-box;
    color: green;
    background-color: #2e96c0;
    border-color: #2e96c0; }

#greeter_infobar {
  border-bottom-width: 0;
  font-weight: bold; }

.nautilus-window paned > separator {
  background-image: linear-gradient(to bottom, rgba(25, 28, 37, 0.95), rgba(25, 28, 37, 0.95)); }

filechooser paned > separator {
  background-image: linear-gradient(to bottom, rgba(25, 28, 37, 0.95), rgba(25, 28, 37, 0.95)); }

filechooser.csd.background, filechooser placessidebar list,
.nautilus-window.csd.background,
.nautilus-window placessidebar list {
  background-color: transparent; }

filechooser placessidebar.sidebar,
.nautilus-window placessidebar.sidebar {
  background-color: rgba(35, 40, 52, 0.95); }
  filechooser placessidebar.sidebar row.sidebar-row,
  .nautilus-window placessidebar.sidebar row.sidebar-row {
    border: none;
    color: """
            + color1
            + """; }
    filechooser placessidebar.sidebar row.sidebar-row .sidebar-icon,
    .nautilus-window placessidebar.sidebar row.sidebar-row .sidebar-icon {
      color: rgba(203, 204, 198, 0.6); }
    filechooser placessidebar.sidebar row.sidebar-row.has-open-popup, filechooser placessidebar.sidebar row.sidebar-row:hover,
    .nautilus-window placessidebar.sidebar row.sidebar-row.has-open-popup,
    .nautilus-window placessidebar.sidebar row.sidebar-row:hover {
      background-color: rgba(203, 204, 198, 0.15); }
    filechooser placessidebar.sidebar row.sidebar-row:disabled, filechooser placessidebar.sidebar row.sidebar-row:disabled label, filechooser placessidebar.sidebar row.sidebar-row:disabled image,
    .nautilus-window placessidebar.sidebar row.sidebar-row:disabled,
    .nautilus-window placessidebar.sidebar row.sidebar-row:disabled label,
    .nautilus-window placessidebar.sidebar row.sidebar-row:disabled image {
      color: rgba(203, 204, 198, 0.4); }
    filechooser placessidebar.sidebar row.sidebar-row:selected.has-open-popup .sidebar-icon, filechooser placessidebar.sidebar row.sidebar-row:selected .sidebar-icon, filechooser placessidebar.sidebar row.sidebar-row:selected:hover .sidebar-icon, filechooser placessidebar.sidebar row.sidebar-row:active:hover .sidebar-icon,
    .nautilus-window placessidebar.sidebar row.sidebar-row:selected.has-open-popup .sidebar-icon,
    .nautilus-window placessidebar.sidebar row.sidebar-row:selected .sidebar-icon,
    .nautilus-window placessidebar.sidebar row.sidebar-row:selected:hover .sidebar-icon,
    .nautilus-window placessidebar.sidebar row.sidebar-row:active:hover .sidebar-icon {
      color: inherit; }
    filechooser placessidebar.sidebar row.sidebar-row:not(:selected) button.sidebar-button,
    .nautilus-window placessidebar.sidebar row.sidebar-row:not(:selected) button.sidebar-button {
      color: """
            + color1
            + """; }
      filechooser placessidebar.sidebar row.sidebar-row:not(:selected) button.sidebar-button:hover,
      .nautilus-window placessidebar.sidebar row.sidebar-row:not(:selected) button.sidebar-button:hover {
        color: """
            + color1
            + """;
        border-color: rgba(10, 12, 15, 0.35);
        background-color: rgba(95, 108, 140, 0.45); }
      filechooser placessidebar.sidebar row.sidebar-row:not(:selected) button.sidebar-button:active,
      .nautilus-window placessidebar.sidebar row.sidebar-row:not(:selected) button.sidebar-button:active {
        color: """
            + color1
            + """;
        border-color: #13161d;
        background-color: """
            + color4
            + """; }
      filechooser placessidebar.sidebar row.sidebar-row:not(:selected) button.sidebar-button:not(:hover):not(:active) > image,
      .nautilus-window placessidebar.sidebar row.sidebar-row:not(:selected) button.sidebar-button:not(:hover):not(:active) > image {
        opacity: 0.5; }
    filechooser placessidebar.sidebar row.sidebar-row.sidebar-new-bookmark-row,
    .nautilus-window placessidebar.sidebar row.sidebar-row.sidebar-new-bookmark-row {
      color: """
            + color4
            + """; }
      filechooser placessidebar.sidebar row.sidebar-row.sidebar-new-bookmark-row .sidebar-icon,
      .nautilus-window placessidebar.sidebar row.sidebar-row.sidebar-new-bookmark-row .sidebar-icon {
        color: inherit; }
    filechooser placessidebar.sidebar row.sidebar-row:drop(active):not(:disabled), filechooser placessidebar.sidebar row.sidebar-row:drop(active):not(:disabled) label, filechooser placessidebar.sidebar row.sidebar-row:drop(active):not(:disabled) .sidebar-icon,
    .nautilus-window placessidebar.sidebar row.sidebar-row:drop(active):not(:disabled),
    .nautilus-window placessidebar.sidebar row.sidebar-row:drop(active):not(:disabled) label,
    .nautilus-window placessidebar.sidebar row.sidebar-row:drop(active):not(:disabled) .sidebar-icon {
      color: #F08437; }
    filechooser placessidebar.sidebar row.sidebar-row:drop(active):not(:disabled):selected,
    .nautilus-window placessidebar.sidebar row.sidebar-row:drop(active):not(:disabled):selected {
      background-color: #F08437; }
      filechooser placessidebar.sidebar row.sidebar-row:drop(active):not(:disabled):selected, filechooser placessidebar.sidebar row.sidebar-row:drop(active):not(:disabled):selected label, filechooser placessidebar.sidebar row.sidebar-row:drop(active):not(:disabled):selected .sidebar-icon,
      .nautilus-window placessidebar.sidebar row.sidebar-row:drop(active):not(:disabled):selected,
      .nautilus-window placessidebar.sidebar row.sidebar-row:drop(active):not(:disabled):selected label,
      .nautilus-window placessidebar.sidebar row.sidebar-row:drop(active):not(:disabled):selected .sidebar-icon {
        color: """
            + color1
            + """; }
  filechooser placessidebar.sidebar separator,
  .nautilus-window placessidebar.sidebar separator {
    background-color: transparent; }

filechooser.maximized placessidebar.sidebar,
.nautilus-window.maximized placessidebar.sidebar {
  background-color: """
            + color2
            + """; }

.nemo-window .sidebar {
  color: """
            + color1
            + """;
  background-color: rgba(35, 40, 52, 0.95); }
  .nemo-window .sidebar .view, .nemo-window .sidebar iconview, .nemo-window .sidebar row {
    background-color: transparent;
    color: """
            + color1
            + """; }
    .nemo-window .sidebar .view.cell:selected, .nemo-window .sidebar iconview.cell:selected, .nemo-window .sidebar row.cell:selected {
      background-color: """
            + color4
            + """;
      color: """
            + color1
            + """; }
    .nemo-window .sidebar .view.expander, .nemo-window .sidebar iconview.expander, .nemo-window .sidebar row.expander {
      color: rgba(123, 126, 129, 0.975); }
      .nemo-window .sidebar .view.expander:hover, .nemo-window .sidebar iconview.expander:hover, .nemo-window .sidebar row.expander:hover {
        color: """
            + color1
            + """; }
  .nemo-window .sidebar separator {
    background-color: transparent; }

.caja-side-pane,
.caja-side-pane > notebook > stack > widget > box,
.caja-side-pane text,
.caja-side-pane treeview {
  color: """
            + color1
            + """;
  caret-color: """
            + color1
            + """;
  background-color: """
            + color2
            + """; }

.caja-side-pane > box button:not(:active):not(:checked) {
  color: """
            + color1
            + """; }

.caja-side-pane .frame {
  border-color: #191c25; }

.caja-side-pane junction {
  background-color: rgba(25, 28, 37, 0.95); }

filechooser actionbar {
  color: """
            + color1
            + """;
  background-color: rgba(35, 40, 52, 0.95);
  border-color: rgba(4, 5, 6, 0.95); }
  filechooser actionbar label, filechooser actionbar combobox {
    color: """
            + color1
            + """; }

.gedit-bottom-panel-paned {
  background-color: """
            + color2
            + """; }

.gedit-side-panel-paned > separator {
  background-image: linear-gradient(to bottom, rgba(25, 28, 37, 0.95), rgba(25, 28, 37, 0.95)); }

.gedit-bottom-panel-paned > separator {
  background-image: linear-gradient(to bottom, #13161d, #13161d); }

.gedit-document-panel {
  background-color: rgba(35, 40, 52, 0.95); }
  .maximized .gedit-document-panel {
    background-color: """
            + color2
            + """; }
  .gedit-document-panel row {
    color: """
            + color1
            + """;
    background-color: rgba(203, 204, 198, 0); }
    .gedit-document-panel row:hover {
      background-color: rgba(203, 204, 198, 0.15); }
    .gedit-document-panel row:active {
      color: """
            + color1
            + """;
      background-color: """
            + color4
            + """; }
      .gedit-document-panel row:active button {
        color: """
            + color1
            + """; }
    .gedit-document-panel row:selected, .gedit-document-panel row:selected:hover {
      color: """
            + color1
            + """;
      background-color: """
            + color4
            + """; }
    .gedit-document-panel row:hover:not(:selected) button:active {
      color: """
            + color1
            + """; }

filechooser actionbar button {
  color: """
            + color1
            + """;
  border-color: rgba(10, 12, 15, 0.35);
  background-color: rgba(80, 92, 119, 0.35); }
  .caja-side-pane > box button:hover:not(:active), filechooser actionbar button:hover {
    color: """
            + color1
            + """;
    border-color: rgba(10, 12, 15, 0.35);
    background-color: rgba(95, 108, 140, 0.45); }
  filechooser actionbar button:active, filechooser actionbar button:checked {
    color: """
            + color1
            + """;
    border-color: rgba(10, 12, 15, 0.35);
    background-color: """
            + color4
            + """; }
  filechooser actionbar button:disabled {
    color: #555960;
    border-color: rgba(10, 12, 15, 0.35);
    background-color: rgba(80, 92, 119, 0.2); }

filechooser actionbar entry {
  color: """
            + color1
            + """;
  border-color: rgba(10, 12, 15, 0.35);
  background-color: rgba(80, 92, 119, 0.35); }
  filechooser actionbar entry image, filechooser actionbar entry image:hover {
    color: inherit; }
  filechooser actionbar entry:focus {
    color: """
            + color1
            + """;
    border-color: rgba(10, 12, 15, 0.35);
    background-color: """
            + color4
            + """; }
  filechooser actionbar entry:disabled {
    color: rgba(203, 204, 198, 0.55);
    background-color: rgba(80, 92, 119, 0.2); }

filechooser placessidebar.sidebar scrollbar,
.nautilus-window placessidebar.sidebar scrollbar, .nemo-window .sidebar scrollbar, .caja-side-pane scrollbar {
  border-color: rgba(25, 28, 37, 0.95); }
  filechooser placessidebar.sidebar scrollbar.overlay-indicator:not(.dragging):not(.hovering) slider,
  .nautilus-window placessidebar.sidebar scrollbar.overlay-indicator:not(.dragging):not(.hovering) slider, .nemo-window .sidebar scrollbar.overlay-indicator:not(.dragging):not(.hovering) slider, .caja-side-pane scrollbar.overlay-indicator:not(.dragging):not(.hovering) slider {
    background-color: #f0f0ee;
    border: 1px solid rgba(0, 0, 0, 0.3); }
  filechooser placessidebar.sidebar scrollbar slider,
  .nautilus-window placessidebar.sidebar scrollbar slider, .nemo-window .sidebar scrollbar slider, .caja-side-pane scrollbar slider {
    background-color: rgba(240, 240, 238, 0.7); }
    filechooser placessidebar.sidebar scrollbar slider:hover,
    .nautilus-window placessidebar.sidebar scrollbar slider:hover, .nemo-window .sidebar scrollbar slider:hover, .caja-side-pane scrollbar slider:hover {
      background-color: #fcfcfc; }
    filechooser placessidebar.sidebar scrollbar slider:hover:active,
    .nautilus-window placessidebar.sidebar scrollbar slider:hover:active, .nemo-window .sidebar scrollbar slider:hover:active, .caja-side-pane scrollbar slider:hover:active {
      background-color: """
            + color4
            + """; }
    filechooser placessidebar.sidebar scrollbar slider:disabled,
    .nautilus-window placessidebar.sidebar scrollbar slider:disabled, .nemo-window .sidebar scrollbar slider:disabled, .caja-side-pane scrollbar slider:disabled {
      background-color: transparent; }
  filechooser placessidebar.sidebar scrollbar trough,
  .nautilus-window placessidebar.sidebar scrollbar trough, .nemo-window .sidebar scrollbar trough, .caja-side-pane scrollbar trough {
    background-color: rgba(25, 28, 37, 0.95); }

@define-color theme_fg_color """
            + color1
            + """;
@define-color theme_text_color """
            + color1
            + """;
@define-color theme_bg_color """
            + color6
            + """;
@define-color theme_base_color """
            + color2
            + """;
@define-color theme_selected_bg_color """
            + color4
            + """;
@define-color theme_selected_fg_color """
            + color1
            + """;
@define-color fg_color """
            + color1
            + """;
@define-color text_color """
            + color1
            + """;
@define-color bg_color """
            + color6
            + """;
@define-color base_color """
            + color2
            + """;
@define-color selected_bg_color """
            + color4
            + """;
@define-color selected_fg_color """
            + color1
            + """;
@define-color insensitive_bg_color #232936;
@define-color insensitive_fg_color alpha(#cbccc6, 0.5);
@define-color insensitive_base_color """
            + color2
            + """;
@define-color theme_unfocused_fg_color """
            + color1
            + """;
@define-color theme_unfocused_text_color """
            + color1
            + """;
@define-color theme_unfocused_bg_color """
            + color6
            + """;
@define-color theme_unfocused_base_color """
            + color2
            + """;
@define-color borders #13161d;
@define-color unfocused_borders #13161d;
@define-color warning_color #F27835;
@define-color error_color #FC4138;
@define-color success_color #73d216;
@define-color placeholder_text_color #A8A8A8;
@define-color link_color #59779b;
@define-color content_view_bg """
            + color2
            + """;
@define-color wm_title alpha(#cfd1c1, 0.8);
@define-color wm_unfocused_title alpha(#cfd1c1, 0.5);
@define-color wm_bg """
            + color6
            + """;
@define-color wm_bg_unfocused #222735;
@define-color wm_highlight #252b39;
@define-color wm_shadow alpha(black, 0.35);
@define-color wm_button_close_bg #cc575d;
@define-color wm_button_close_hover_bg #d7787d;
@define-color wm_button_close_active_bg #be3841;
@define-color wm_icon_close_bg #2f343f;
@define-color wm_button_hover_bg #454C5C;
@define-color wm_button_active_bg """
            + color4
            + """;
@define-color wm_button_hover_border #262932;
@define-color wm_icon_bg #90939B;
@define-color wm_icon_unfocused_bg #666A74;
@define-color wm_icon_hover_bg #C4C7CC;
@define-color wm_icon_active_bg """
            + color1
            + """;
"""
        )
        rofi_file.writelines(rofi_file_data)
