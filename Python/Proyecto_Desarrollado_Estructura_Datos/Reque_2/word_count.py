texto = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ac volutpat mi. Etiam elementum lacus at ligula efficitur efficitur. Nam ut vulputate sem. Duis elementum mauris vel posuere interdum. Vestibulum nisl enim, molestie in lacus scelerisque, bibendum fringilla mi. Etiam augue ex, tempor non diam vitae, consectetur interdum ex. Vestibulum consequat, mauris at luctus iaculis, urna arcu placerat risus, ut efficitur nulla lectus non mi. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Maecenas a velit mollis, dapibus orci nec, egestas tellus. Morbi ullamcorper dolor et purus sollicitudin eleifend. Fusce a mauris id elit tempus suscipit sit amet vel sapien. Nunc eget augue sit amet tellus sodales commodo eget a turpis. Vestibulum vel suscipit urna, eget mattis orci. Mauris velit ex, convallis eu nibh quis, pretium ullamcorper magna.

Curabitur facilisis eleifend sapien, nec suscipit magna euismod quis. Integer dolor dui, consequat vel ullamcorper eu, maximus vitae leo. Proin eu mi rutrum, lacinia purus in, cursus turpis. Maecenas commodo arcu nunc, et ornare nunc luctus sed. Proin scelerisque ornare erat, vel porta urna sollicitudin a. Duis eleifend dolor orci, id vestibulum nunc vestibulum at. Praesent vel ligula elit. Quisque quis imperdiet libero, ac sollicitudin sem. Sed leo ante, porttitor eget feugiat eu, convallis vitae arcu. Aenean lacus sem, dictum sit amet felis ut, laoreet ornare turpis. Etiam aliquet lectus sed odio condimentum, scelerisque viverra enim tempus. Mauris eu eleifend massa, in fringilla turpis. Donec leo libero, consectetur at tellus ac, faucibus fermentum eros. Curabitur pellentesque est id lectus pellentesque, eget scelerisque nisi ornare. Duis molestie condimentum ex ac mollis.

Sed erat neque, fermentum a suscipit in, ullamcorper eu urna. Nunc vitae dui non nunc luctus iaculis. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Vivamus et nunc risus. Ut posuere dui sit amet purus consequat maximus. Morbi aliquam ipsum non erat malesuada tristique vel eget metus. Curabitur non mauris id sem imperdiet maximus. Aliquam tincidunt tristique scelerisque. Mauris ipsum leo, consequat sed euismod non, lacinia a tellus. Sed fringilla nulla mauris, nec elementum diam faucibus id. Maecenas tincidunt elit a massa sollicitudin, ac auctor arcu egestas. Praesent eu aliquet dui. Cras cursus eros aliquam rhoncus volutpat. Integer a turpis eros.

Nulla rutrum ex vel tortor luctus, quis consequat eros facilisis. Morbi sollicitudin a nibh condimentum fringilla. Morbi efficitur orci dolor, vel mollis felis aliquam id. Nunc vel neque eget dui sagittis venenatis non eget augue. Praesent at leo viverra, tempus libero vel, vehicula neque. Interdum et malesuada fames ac ante ipsum primis in faucibus. Quisque ut dignissim libero, vitae tempor felis. Mauris ut suscipit sem. Vestibulum tempor at mauris faucibus tristique. Nunc pulvinar elit eget arcu dapibus iaculis.

Proin lectus nunc, tincidunt et porta sed, aliquet ut mi. Fusce laoreet, tellus at suscipit tincidunt, nisl nibh consectetur augue, eget semper eros libero quis dolor. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. In sollicitudin egestas ante, condimentum lobortis diam posuere quis. Ut at lorem a eros lacinia varius ut in purus. Fusce tempus gravida maximus. Duis maximus, dolor porta porta pretium, lorem elit pulvinar tortor, vitae tempor mi purus a velit."""

# Eliminamos los caracteres no alfanuméricos y dividimos el texto en palabras
palabras = texto.split()

# Contamos los caracteres distintos
caracteres_distintos = len(set(texto))

# Contamos las palabras distintas
palabras_distintas = len(set(palabras))

# Imprimimos los resultados
print(f"El número de caracteres distintos es: {caracteres_distintos}")
print(f"El número de palabras distintas es: {palabras_distintas}")

