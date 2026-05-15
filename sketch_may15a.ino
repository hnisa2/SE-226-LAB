int LED0pin = 46;
int LED1pin = 45;
int LED2pin = 44;
int LED3pin = 43;

int button1pin = 38;  
int button2pin = 39;  

bool systemON = false;
int mode = 1;

bool lastButton1 = HIGH;
bool lastButton2 = HIGH;

unsigned long previousTime = 0;
int interval = 1000;

bool blinkState = false;
int currentLED = 0;

void setup() {
  pinMode(LED0pin, OUTPUT);
  pinMode(LED1pin, OUTPUT);
  pinMode(LED2pin, OUTPUT);
  pinMode(LED3pin, OUTPUT);

  pinMode(button1pin, INPUT_PULLUP);
  pinMode(button2pin, INPUT_PULLUP);

  allOFF();
}

void loop() {
  bool button1 = digitalRead(button1pin);
  bool button2 = digitalRead(button2pin);

  if (button1 == LOW && lastButton1 == HIGH) {
    systemON = !systemON;

    if (systemON == true) {
      mode = 1;
      blinkState = false;
      currentLED = 0;
      previousTime = millis();
    }

    allOFF();
    delay(200);
  }

  if (button2 == LOW && lastButton2 == HIGH) {
    mode++;

    if (mode > 3) {
      mode = 1;
    }

    allOFF();
    currentLED = 0;
    blinkState = false;
    previousTime = millis();

    delay(200);
  }

  lastButton1 = button1;
  lastButton2 = button2;

  if (systemON == false) {
    allOFF();
    return;
  }

  if (mode == 1) {
    mode1();
  }
  else if (mode == 2) {
    mode2();
  }
  else if (mode == 3) {
    mode3();
  }
}

void allON() {
  digitalWrite(LED0pin, HIGH);
  digitalWrite(LED1pin, HIGH);
  digitalWrite(LED2pin, HIGH);
  digitalWrite(LED3pin, HIGH);
}

void allOFF() {
  digitalWrite(LED0pin, LOW);
  digitalWrite(LED1pin, LOW);
  digitalWrite(LED2pin, LOW);
  digitalWrite(LED3pin, LOW);
}

void mode1() {
  unsigned long currentTime = millis();

  if (currentTime - previousTime >= interval) {
    previousTime = currentTime;

    blinkState = !blinkState;

    if (blinkState == true) {
      allON();
    }
    else {
      allOFF();
    }
  }
}
void mode2() {
  unsigned long currentTime = millis();

  if (currentTime - previousTime >= interval) {
    previousTime = currentTime;

    allOFF();

    if (currentLED == 0) {
      digitalWrite(LED0pin, HIGH);
    }
    else if (currentLED == 1) {
      digitalWrite(LED1pin, HIGH);
    }
    else if (currentLED == 2) {
      digitalWrite(LED2pin, HIGH);
    }
    else if (currentLED == 3) {
      digitalWrite(LED3pin, HIGH);
    }

    currentLED++;

    if (currentLED > 3) {
      currentLED = 0;
    }
  }
}

void mode3() {
  unsigned long currentTime = millis();

  if (currentTime - previousTime >= interval) {
    previousTime = currentTime;

    allOFF();

    if (currentLED == 0) {
      digitalWrite(LED3pin, HIGH);
    }
    else if (currentLED == 1) {
      digitalWrite(LED2pin, HIGH);
    }
    else if (currentLED == 2) {
      digitalWrite(LED1pin, HIGH);
    }
    else if (currentLED == 3) {
      digitalWrite(LED0pin, HIGH);
    }

    currentLED++;

    if (currentLED > 3) {
      currentLED = 0;
    }
  }
}