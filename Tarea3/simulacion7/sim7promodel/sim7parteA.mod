��gBw@�Ub@���W}��9 simulacion 7   8         7 C:\Users\spere\Documents\ProModel\Output\sim7parteA.RESJ C:\Program Files (x86)\ProModel Corporation\ProModel\9.3\Graphics\BANK.GLB 20                         ���          ���     {�G�z�?      �?      �  �            �?            Baseline                  Espera_en_fila_acumulada 0        Tipo_de_transaccion     Tiempo_de_llegada          Elegir_transaccion  15 1 29 2 32 3 24 4    Cliente       150   ���@���A    +                      2 6.4286            Cajero_1               %IA۶]A    ` K   "   h   <        %I"A�$�A   g �   F   m   +        ۶�A�$iA    ^ �   h   _   N        I�d@�$�@    t �   L   �   J        �   �    �   "    ����            �      "Courier New                      Cajero 1���     <   �����   +                    <   ����� �    1                       Entrada_banco                 60 36.000       �  }   �    �  ���        ����            �      "Courier New                     ��     �       p  �  �       p  t"    INFINITE                        Cajero_2                 �@�m+A    ` 6  8   8  F        %IAn�vA     ?  <   <  )        n�vAn�VA          1  R        I�d@�$�@    t m  S   m  M        v  '    �  �    ����            �      "Courier New                      Cajero 2���       �����  ,                      ����� �    1                        Cajero_3                 �@�m+A    ` W  K   �  I        �$	An�vA     �  U   �  .        n�vAn�VA     �  =   �  O        I�d@�$�@    t #  M      H        A  �    4  +    ����            �      "Courier New                      Cajero 3���     �  ����u  /                    �  ����� �    1                        Cajero_4                 �@�m+A    ` �  I   �  I        I�$A�$YA   * �  ?   �  .        %I�A�$YA    ^ �  3   �  S        I�d@�$�@    t �  U   �  Q        �  �    �  +    ����            �      "Courier New                      Cajero 4���     f  ����&  0                    f  ����� �    1                        Cajero_5                 �@�m+A    ` W  J   W  J        n�A۶�A    : Q  '   Z  (        n�vAn�VA     I  @   L  T        I�d@�$�@    t �  Z   �  N        �  +    �  �    ����            �      "Courier New                      Cajero 5���        �����  2                       ����� �    1                        Cajero_6                 �@�m+A    `   Q     Q        n�A۶}A       !     2        n�vAn�VA       D     ]        I�d@�$�@    t C  ^   C  W        N  /    c  �    ����            �      "Courier New                      Cajero 6���     �  �����  2                    �  ����� �    1                            E(20) INF 1 0 ( Tipo_de_transaccion=Elegir_transaccion()                                                         Tiempo_de_llegada=Clock(min)                       ~  �   �      1                           ~  X  �      1                            ~  �  �      1                            ~  |  �      1                            ~    �      1                            ~  �  �      1            P Espera_en_fila_acumulada=Espera_en_fila_acumulada+(Clock(min)-Tiempo_de_llegada)   If Tipo_de_transaccion = 1 Then { 	Wait E(45) }$ Else If Tipo_de_transaccion = 2 Then { 	Wait E(75) }$ Else If Tipo_de_transaccion = 3 Then { 	Wait E(120) } Else Wait E(180)                          1          P Espera_en_fila_acumulada=Espera_en_fila_acumulada+(Clock(min)-Tiempo_de_llegada)   If Tipo_de_transaccion = 1 Then { 	Wait E(45) }$ Else If Tipo_de_transaccion = 2 Then { 	Wait E(75) }$ Else If Tipo_de_transaccion = 3 Then { 	Wait E(120) } Else Wait E(180)                          1          P Espera_en_fila_acumulada=Espera_en_fila_acumulada+(Clock(min)-Tiempo_de_llegada)   If Tipo_de_transaccion = 1 Then { 	Wait E(45) }$ Else If Tipo_de_transaccion = 2 Then { 	Wait E(75) }$ Else If Tipo_de_transaccion = 3 Then { 	Wait E(120) } Else Wait E(180)                          1          P Espera_en_fila_acumulada=Espera_en_fila_acumulada+(Clock(min)-Tiempo_de_llegada)   If Tipo_de_transaccion = 1 Then { 	Wait E(45) }$ Else If Tipo_de_transaccion = 2 Then { 	Wait E(75) }$ Else If Tipo_de_transaccion = 3 Then { 	Wait E(120) } Else Wait E(180)                          1          P Espera_en_fila_acumulada=Espera_en_fila_acumulada+(Clock(min)-Tiempo_de_llegada)   If Tipo_de_transaccion = 1 Then { 	Wait E(45) }$ Else If Tipo_de_transaccion = 2 Then { 	Wait E(75) }$ Else If Tipo_de_transaccion = 3 Then { 	Wait E(120) } Else Wait E(180)                          1          P Espera_en_fila_acumulada=Espera_en_fila_acumulada+(Clock(min)-Tiempo_de_llegada)   If Tipo_de_transaccion = 1 Then { 	Wait E(45) }$ Else If Tipo_de_transaccion = 2 Then { 	Wait E(75) }$ Else If Tipo_de_transaccion = 3 Then { 	Wait E(120) } Else Wait E(180)                          1      ��gB           PR����   ���    ���        A �$D  �C �/DPR             ���        �@ �-D  �C @3D ��� ���    �    �                 ����            �      Times New Roman                  ENTRADA DEL BANCO                       