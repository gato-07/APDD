from apdClass import APDDeterminista
def probar_apd_determinista():
    transiciones = {
        ('q0', 'a', 'R'): ('q0', 'AR'),
        ('q0', 'a', 'A'): ('q0', 'AA'),
        ('q0', 'b', 'A'): ('q1', ''),       # desapila A
        ('q1', 'b', 'A'): ('q1', ''),       # desapila A
        ('q1', None, 'R'): ('qf', '')       # transición épsilon, desapila R
    }

    apd = APDDeterminista.construir_apd(
        estados={'q0', 'q1', 'qf'},
        alfabeto_entrada={'a', 'b'},
        alfabeto_pila={'A', 'R'},
        estado_inicial='q0',
        estados_aceptacion={'qf'},
        transiciones=transiciones
    )

    casos = [
        # palabra, espera_pila_vacia, espera_estado_final
        ("", True, True),
        ("ab", True, True),
        ("aabb", True, True),
        ("aaabbb", True, True),
        ("aaaabbbb", True, True),
        ("aab", False, False),       # más 'a' que 'b'
        ("abb", False, False),       # más 'b' que 'a'
        ("aaabb", False, False),
        ("aaabbbb", False, False),
        ("a", False, False),
        ("b", False, False),
        ("abab", False, False),      # no apila ni desapila correctamente
    ]

    for palabra, espera_stack, espera_final in casos:
        resultado_stack = apd.apd_logic(True, palabra)
        resultado_final = apd.apd_logic(False, palabra)
        assert resultado_stack == espera_stack, f"Falla por pila: {palabra}"
        assert resultado_final == espera_final, f"Falla por estado: {palabra}"

    print("✅ Todas las pruebas pasaron correctamente.")

# Ejecutar test
probar_apd_determinista()