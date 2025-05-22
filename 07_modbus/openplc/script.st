PROGRAM TrafficLight
  VAR
    Counter AT %IW0 : INT := 0;

    RedLight AT %QX0.0 : BOOL := TRUE;
    YellowLight AT %QX0.1 : BOOL := FALSE;
    GreenLight AT %QX0.2 : BOOL := FALSE;

  END_VAR

  Counter := Counter + 1;
  IF Counter < 400 THEN
    RedLight := TRUE;
    YellowLight := FALSE;
    GreenLight := FALSE;
  ELSIF Counter < 500 THEN
    RedLight := FALSE;
    YellowLight := TRUE;
    GreenLight := FALSE;
  ELSIF Counter < 1000 THEN
    RedLight := FALSE;
    YellowLight := FALSE;
    GreenLight := TRUE;
  ELSE
    Counter := 0;
  END_IF;
  

END_PROGRAM


CONFIGURATION Config0

  RESOURCE Res0 ON PLC
    TASK task0(INTERVAL := T#50ms,PRIORITY := 0);
    PROGRAM instance0 WITH task0 : TrafficLight;
  END_RESOURCE
END_CONFIGURATION