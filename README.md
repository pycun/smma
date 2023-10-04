## Sincronismo, Multiprocesos, Multihilos y Asincronismo... con Python

**Presentación:** https://docs.google.com/presentation/d/1dR9-Z9l11zZq1i7R0LIZ49ztEn_iscgNSBRcek73Ed0/edit?usp=sharing

## Pasos para Ejecutar Ejemplos

### Paso 1: Clonar proyecto

```shell
git clone https://github.com/pycun/smma.git
```

### Paso 2: Crear entorno

Debe ser con Python mayor a 3.5

```shell
virtualenv env_smma -p 3.8
```

### Paso 3: Instalar Dependencias

```shell
pip install -r requirements.txt
```

### Paso 4: Ejecutar Ejemplos

#### Ejemplo 1: Uso de RAM

En este ejemplo podremos ver como nuestro uso RAM aumenta

```shell
python ram.py
```

#### Ejemplo 2: Uso de CPU

En este ejemplo podremos ver como nuestro uso CPU aumenta

```shell
python cpu.py
```

#### Ejemplo 3: Diferencia entre ejecutar codigo secuencial a concurrente

Ejemplo de codigo secuencial, codigo que mueve dinero de una Cuenta A a una Cuenta B, lo mismo que le quita a una, se lo agrega a la otra, dado que se ejecuta sobre el mismo hilo la suma de ambas siempre debe dar el mismo resultado, en este caso 2000

```shell
python banco_sincrono.py
```


Ejemplo de codigo concurrente, codigo que mueve dinero de una Cuenta A a una Cuenta B, lo mismo que le quita a una, se lo agrega a la otra, dado que se ejecuta sobre diferentes hilos la suma de ambas puede que no sea el resultado esperado, en este caso 2000

```shell
python banco_concurrente.py
```