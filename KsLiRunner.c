#include <wiringPi.h> //подключаем заголовочный файл библиотеки
int main (void)
{
  wiringPiSetup () ; //инициализируем библиотеку
  pinMode (0, OUTPUT) ;
  for (;;)
  {
    digitalWrite (0, HIGH) ; delay (500) ;
    digitalWrite (0,  LOW) ; delay (500) ;
  }
  return 0 ;
}