from sense_hat import SenseHat

#orientation
sense=SenseHat()
orientation = sense.get_orientation()
print("p: {pitch}, r: {roll}, y: {yaw}".format(**orientation))

#compass
sense.set_imu_config(True, False, False)  # enable only the compass
north = sense.get_compass()
print("North: %s" % north)

#gyroscope
sense.set_imu_config(False, True, False)  # gyroscope only
gyro_only = sense.get_gyroscope()
print("p: {pitch}, r: {roll}, y: {yaw}".format(**gyro_only))

#accelerometer
sense.set_imu_config(False, False, True)  # accelerometer only
accel_only = sense.get_accelerometer()
print("p: {pitch}, r: {roll}, y: {yaw}".format(**accel_only))
