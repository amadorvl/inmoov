def daVinci():
  inMoov.setHandVelocity("left", -1.0, -1.0, -1.0, -1.0, -1.0, 23)
  inMoov.setHandVelocity("right", 1.0, 1.0, 1.0, 1.0, 1.0, 23)
  inMoov.setArmVelocity("left", 30, 30, 30, 30)
  inMoov.setArmVelocity("right", 30, 30, 30, 30)
  inMoov.setHeadVelocity(30, 30)
  inMoov.moveHead(80,90)
  inMoov.moveArm("left",0,118,13,74)
  inMoov.moveArm("right",0,118,29,74)
  inMoov.moveHand("left",50,28,30,10,10,47)
  inMoov.moveHand("right",10,10,10,10,10,137)