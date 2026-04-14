from browser import window


# -----------------------------
# PARSER
# -----------------------------
def parse_svg(svg_str):
    parser = window.DOMParser.new()
    doc = parser.parseFromString(svg_str, "image/svg+xml")
    return doc.documentElement


# -----------------------------
# NORMALIZAÇÃO DE VALORES
# -----------------------------
def normalize_numeric(value):
    """Remove espaços, unidades e normaliza números para comparação."""
    if value is None:
        return value
    
    v = value.strip()

    # remove px
    if v.endswith("px"):
        v = v[:-2]

    # normaliza número (ex: "1.0" -> "1")
    try:
        num = round(float(v), 3)
        if num.is_integer():
            return str(int(num))
        return str(num)
    except ValueError:
        window.console.log(f"Valor não numérico: '{value}'")
        return v

# -----------------------------
# NORMALIZAÇÃO DE STYLE
# -----------------------------
def normalize_style(node):
    """Normaliza a string de estilo, ordenando propriedades e normalizando valores numéricos."""
    style = node.getAttribute("style")
    if not style:
        return
    
    props = {}

    for item in style.split(";"):
        if ":" in item:
            k, v = item.split(":", 1)
            k = k.strip().lower()
            try:
                v = normalize_numeric(v.strip())
            except ValueError:
                window.console.warn(f"Valor não numérico para '{k}': '{v}' - mantendo original")
            props[k] = v

    # ordena propriedades
    normalized = "; ".join(f"{k}: {props[k]}" for k in sorted(props))
    node.setAttribute("style", normalized)


# -----------------------------
# NORMALIZAÇÃO DE ATRIBUTOS
# -----------------------------
def normalize_attributes(node):
    """Normaliza os atributos do elemento, ordenando-os e normalizando valores numéricos."""
    
    def sort_attributes(attrs):
        attrs.sort(key=lambda x: x[0])

    def get_normalized_attrs(node):
        attrs = []
        for attr in node.attributes:
            name = attr.name.lower()
            value = attr.value.strip()

            if name in ["x1", "y1", "x2", "y2", "width", "height", "cx", "cy", "r", "to", "from"]:
                value = normalize_numeric(value)

            attrs.append((name, value))

        return attrs

    def merge_attrs(node, attrs):
        for attr in list(node.attributes):
            node.removeAttribute(attr.name)

        for name, value in attrs:
            node.setAttribute(name.lower(), value)


    if not node.attributes:
        return

    attrs = get_normalized_attrs(node)
    sort_attributes(attrs)
    merge_attrs(node, attrs)



def normalize_tag_name(node):
    # apenas elementos (ignora text nodes)
    if not hasattr(node, "tagName"):
        return
    
    current = node.tagName
    normalized = current.lower()

    if current != normalized:
        # recria o elemento com o novo nome
        doc = node.ownerDocument
        new_node = doc.createElementNS(node.namespaceURI, normalized)

        # copia atributos
        if node.attributes:
            for attr in node.attributes:
                new_node.setAttribute(attr.name, attr.value)

        # move filhos
        while node.firstChild:
            new_node.appendChild(node.firstChild)

        # substitui no pai
        parent = node.parentNode
        if parent:
            parent.replaceChild(new_node, node)

        return new_node

    return node

# -----------------------------
# NORMALIZAÇÃO RECURSIVA
# -----------------------------
def normalize_node(node):
    # normaliza a própria tag
    node = normalize_tag_name(node)

    node.normalize()  # junta text nodes

    normalize_style(node)
    normalize_attributes(node)

    # filhos (inclui elementos SVG como animate)
    for child in node.children:
        normalize_node(child)

    return node

# -----------------------------
# SERIALIZAÇÃO
# -----------------------------
def serialize(node):
    serializer = window.XMLSerializer.new()
    return serializer.serializeToString(node)


# -----------------------------
# COMPARAÇÃO FINAL
# -----------------------------
def svg_equal(svg1, svg2):
    n1 = parse_svg(svg1)
    n2 = parse_svg(svg2)

    n1 = normalize_node(n1)
    n2 = normalize_node(n2)

    window.console.log(f'n1.isEqualNode(n2): {n1.isEqualNode(n2)}')

    window.console.log(f'Serialized SVG 1: {serialize(n1)}')
    window.console.log(f'Serialized SVG 2: {serialize(n2)}')

    return n1.isEqualNode(n2)