{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "079 - Arrays de Alta Performance.ipynb",
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "cDyLL9ABN4t-"
      },
      "source": [
        "## PROGRAMAÇÃO EM PYTHON - FERNANDO FELTRIN"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "UWnTvc_cP0CA"
      },
      "source": [
        ooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKAP/Z)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "UzhySSkGOPIO"
      },
      "source": [
        "[Compre já em Amazon.com](https://www.amazon.com.br/s?i=digital-text&rh=p_27%3AFernando+Feltrin&s=relevancerank&text=Fernando+Feltrin&ref=dp_byline_sr_ebooks_1)\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "fXJYpuJcHyWh"
      },
      "source": [
        "## Arrays de Alta Performance"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "lDTDjtiIuYTL"
      },
      "source": [
        "Arrays de alta performance"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "eNPpmAiWmBJq",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "c3a9e49b-5983-4aef-d382-fac145c267c5"
      },
      "source": [
        "from array import *\n",
        "\n",
        "array1 = array('f', [1,2,3,4,5,6,7,8,9,10])\n",
        "\n",
        "print(array1)\n",
        "print(type(array1))\n",
        "\n",
        "# Tabela dos principais typecodes\n",
        "\n",
        "# b Representa um número inteiro de 1 byte\n",
        "# h Representa um número inteiro de 2 bytes\n",
        "# c Representa um caractere de 1 byte\n",
        "# u Representa um caractere unicode de 2 bytes\n",
        "# w Representa um caractere unicode de 4 bytes\n",
        "# f Representa um número float de 4 bytes\n",
        "# d Representa um número float de 8 bytes\n",
        "\n",
        "# especificando o tipo de dado que consta em uma lista pode se reduzir drasticamente seu tamanho em memória\n"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "array('f', [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0])\n",
            "<class 'array.array'>\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "12xzbr9MIu92"
      },
      "source": [
        "Arrays Numpy"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "vuFdlPDprqIa"
      },
      "source": [
        "import numpy as np"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "TOD6Mi-UXGKR",
        "outputId": "76351bcd-3a76-4d4f-8abc-d3ddd72e5896"
      },
      "source": [
        "Tipagem de dados Numpy\n",
        "\n",
        "data = np.array([[122, 183, 115],[420, 111, 128]])\n",
        "# Dados automaticamente identificados como do tipo int\n",
        "\n",
        "print(data)\n",
        "print(type(data))\n",
        "print(data.dtype)\n"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[[122 183 115]\n",
            " [420 111 128]]\n",
            "<class 'numpy.ndarray'>\n",
            "int64\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "n2CcNXsztJS-",
        "outputId": "9933cac4-c4ca-4405-f651-eb709f33988b"
      },
      "source": [
        "data = np.array([[122, 183, 115],[420, 111, 128]], dtype = 'int')\n",
        "# Dados manualmente definidos como do tipo int\n",
        "\n",
        "print(data)\n",
        "print(type(data))\n",
        "print(data.dtype)\n"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[[122 183 115]\n",
            " [420 111 128]]\n",
            "<class 'numpy.ndarray'>\n",
            "int64\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bvDEZ7Y8XGMl",
        "outputId": "8ef3a6c3-d96a-44b6-c9cd-f0ee9b3acff6"
      },
      "source": [
        "data = np.array([[122, 183, 115],[420, 111, 128]], dtype = 'float')\n",
        "# Dados inicialmente declarados como int, porém definidos como float passarão\n",
        "# a ter suas respectivas casas decimais consideradas\n",
        "\n",
        "print(data)\n",
        "print(type(data))\n",
        "print(data.dtype)\n"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[[122. 183. 115.]\n",
            " [420. 111. 128.]]\n",
            "<class 'numpy.ndarray'>\n",
            "float64\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "awNf2RwqtsAV",
        "outputId": "00a16c64-58fe-401d-bed4-9a9284aa3c6e"
      },
      "source": [
        "data = np.array([[122.4, 183.7, 115.0],[420.1, 111.9, 128.0]], dtype = 'int')\n",
        "# Dados manualmente definidos como do tipo int, passando a ter seus valores\n",
        "# decimais ignorados pelo interpretador\n",
        "\n",
        "print(data)\n",
        "print(type(data))\n",
        "print(data.dtype)\n"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[[122 183 115]\n",
            " [420 111 128]]\n",
            "<class 'numpy.ndarray'>\n",
            "int64\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "cCqh4U0uXGOs",
        "outputId": "8485babd-5d9f-45ae-da0a-b3927a238f6e"
      },
      "source": [
        "data = np.array([['122', '183', '115'],['420', '111', '128']])\n",
        "# Dados automaticamente identificados como string pela sintaxe\n",
        "\n",
        "print(data)\n",
        "print(type(data))\n",
        "print(data.dtype)\n"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[['122' '183' '115']\n",
            " ['420' '111' '128']]\n",
            "<class 'numpy.ndarray'>\n",
            "<U3\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PnbEjKNBsiib",
        "outputId": "3da87d17-4996-4a14-9447-5b8d0fb52394"
      },
      "source": [
        "data = np.array([[True, True, False],[False, False, True]])\n",
        "\n",
        "print(data)\n",
        "print(type(data))\n",
        "print(data.dtype)\n"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[[ True  True False]\n",
            " [False False  True]]\n",
            "<class 'numpy.ndarray'>\n",
            "bool\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "HcS79tdCQ-nc"
      },
      "source": [
        "Performance de uma array Numpy comparado a uma array padrão do Python"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "73uDQFeDsipR",
        "outputId": "1ed63687-0f47-4e97-edcb-91c1403520f6"
      },
      "source": [
        "array_numpy = np.arange(2000)\n",
        "\n",
        "%timeit array_numpy\n"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "The slowest run took 635.30 times longer than the fastest. This could mean that an intermediate result is being cached.\n",
            "10000000 loops, best of 5: 27.4 ns per loop\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QH6TTMogsirY",
        "outputId": "177efc53-1a61-4cf0-a766-746419683d92"
      },
      "source": [
        "array_python = range(2000)\n",
        "\n",
        "%timeit [array_python[i] for i in array_python]"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "1000 loops, best of 5: 311 µs per loop\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}