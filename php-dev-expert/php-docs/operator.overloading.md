# Métodos Mágicos de Sobrecarga de Operadores

> **Fonte / Source:** https://www.php.net/manual/pt_BR/operator.overloading.php

---

# Métodos Mágicos de Sobrecarga de Operadores

The operator overloading extension allows you to define how an object reacts to operators. This is done by implementing the following magic methods:

Operadores aritméticos:

- `$a::__add($b)`
- `$a::__sub($b)`
- `$a::__mul($b)`
- `$a::__div($b)`
- `$a::__mod($b)`
- `$a::__pow($b)`

Operadores de atribuição:

- `$a::__assign($b)`
- `$a::__assign_add($b)`
- `$a::__assign_sub($b)`
- `$a::__assign_mul($b)`
- `$a::__assign_div($b)`
- `$a::__assign_mod($b)`
- `$a::__assign_pow($b)`
- `$a::__assign_bw_and($b)`
- `$a::__assign_bw_or($b)`
- `$a::__assign_bw_xor($b)`
- `$a::__assign_sl($b)`
- `$a::__assign_sr($b)`
- `$a::__assign_concat($b)`

Operadores binários:

- `$a::__bw_and($b)`
- `$a::__bw_or($b)`
- `$a::__bw_xor($b)`
- `$a::__bw_not()`
- `$a::__sl($b)`
- `$a::__sr($b)`

Operadores de comparação:

- `$a::__is_equal($b)`
- `$a::__is_not_equal($b)`
- `$a::__is_identical($b)`
- `$a::__is_not_identical($b)`
- `$a::__is_smaller($b)`
- `$a::__is_smaller_or_equal($b)`
- `$a::__is_greater($b)`
- `$a::__is_greater_or_equal($b)`
- `$a::__spaceship($b)`

Operadores de incremento e decremento:

- `$a::__pre_inc()`
- `$a::__post_inc()`
- `$a::__pre_dec()`
- `$a::__post_dec()`

Operadores de string:

- `$a::__concat($b)`

## Exemplos de Sobrecarga de Operadores

O exemplo a seguir é a classe usada nos testes da extensão de sobrecarga de operadores.
Ela sobrecarrega todos os operadores que podem ser sobrecarregados.

**Exemplo #1 Classe completa para sobrecarga de operadores**

```
<?php
class OperatorOverloading {
    protected mixed $value;

    // Região de métodos mágicos padrão
    public function __get(string $name)
    {
        return $this->value;
    }

    public function __set(string $name, mixed $value)
    {
        $this->value = $value;
    }

    public function __construct(mixed $init = null)
    {
        $this->value = $init;
    }
    // fim da região

    // região dos operadores artiméticos
    public function __add(mixed $val): int|float
    {
        return $this->value + $val;
    }

    public function __div(mixed $val): int|float
    {
        return $this->value / $val;
    }

    public function __mod(mixed $val): int
    {
        return $this->value % $val;
    }

    public function __mul(mixed $val): int|float
    {
        return $this->value * $val;
    }

    public function __pow(mixed $val): int|float
    {
        return $this->value ** $val;
    }

    public function __sub(mixed $val): int|float
    {
        return $this->value - $val;
    }
    // fim da região

    // região dos operadores de atribuição
    public function __assign(mixed $val): mixed
    {
        return $this->value = $val;
    }

    public function __assign_add(mixed $val): mixed
    {
        return $this->value += $val;
    }

    public function __assign_bw_and(mixed $val): mixed
    {
        return $this->value &= $val;
    }

    public function __assign_bw_or(mixed $val): mixed
    {
        return $this->value |= $val;
    }

    public function __assign_concat(mixed $val): string
    {
        return $this->value .= $val;
    }

    public function __assign_div(mixed $val): mixed
    {
        return $this->value /= $val;
    }

    public function __assign_mod(mixed $val): mixed
    {
        return $this->value %= $val;
    }

    public function __assign_mul(mixed $val): mixed
    {
        return $this->value *= $val;
    }

    public function __assign_pow(mixed $val): mixed
    {
        return $this->value **= $val;
    }

    public function __assign_sl(mixed $val): mixed
    {
        return $this->value <<= $val;
    }

    public function __assign_sr(mixed $val): mixed
    {
        return $this->value >>= $val;
    }

    public function __assign_sub(mixed $val): mixed
    {
        return $this->value -= $val;
    }
    //fim da região

    // região dos operadores binários
    public function __bw_and(mixed $val): int
    {
        return $this->value & $val;
    }

    public function __bw_not(): int|string
    {
        return ~$this->value;
    }

    public function __bw_or(mixed $val): int
    {
        return $this->value | $val;
    }

    public function __bw_xor(mixed $val): int
    {
        return $this->value ^ $val;
    }

    public function __sl(mixed $val): int
    {
        return $this->value << $val;
    }

    public function __sr(mixed $val): int
    {
        return $this->value >> $val;
    }
    // fim da região

    // região dos operadores de comparação
    public function __is_equal(mixed $val): bool
    {
        return $this->value == $val;
    }

    public function __is_greater(mixed $val): bool
    {
        return $this->value > $val;
    }

    public function __is_greater_or_equal(mixed $val): bool
    {
        return $this->value >= $val;
    }

    public function __is_identical(mixed $val): bool
    {
        return $this->value === $val;
    }

    public function __is_not_equal(mixed $val): bool
    {
        return $this->value != $val;
    }

    public function __is_not_identical(mixed $val): bool
    {
        return $this->value !== $val;
    }

    public function __is_smaller(mixed $val): bool
    {
        return $this->value < $val;
    }

    public function __is_smaller_or_equal(mixed $val): bool
    {
        return $this->value <= $val;
    }

    public function __spaceship(mixed $val): int
    {
        return $this->value <=> $val;
    }
    // fim da região

    // região dos operadores de incremento/decremento
    public function __post_dec(): mixed
    {
        return $this->value--;
    }

    public function __post_inc(): mixed
    {
        return $this->value++;
    }

    public function __pre_dec(): mixed
    {
        return --$this->value;
    }

    public function __pre_inc(): mixed
    {
        return ++$this->value;
    }
    // fim da região

    // região dos operadores de string
    public function __concat(mixed $val): string
    {
        return $this->value . $val;
    }
    // fim da região

}
```

Usando a classe acima pode-se sobrecarregar os operadores da seguinte forma:

```
<?php
$a = new OperatorOverloading(5);
var_dump($a + 10);
var_dump($a - 10);
$b = new OperatorOverloading("Olá, ");
var_dump($b . "Mundo!");
```

The above code will output:

```
int(15)
int(-5)
string(11) "Olá, Mundo!"
```

`↑` and `↓` to navigate •
`Enter` to select •
`Esc` to close • `/` to open

document.addEventListener("DOMContentLoaded", function() {
/\*{{{Search Modal\*/
const language = 'local';
initSearchModal();
initPHPSearch(language).then((searchCallback) => {
initSearchUI({language, searchCallback, limit: 30});
});
/\*}}}\*/
});
