" This files contains tests to verify that the reference_frame_transfer.py script works correctly"
" The file checks that using the functions defined in the reference_frame_transfer.py yields the same results as using "
" external calculations"
import referece_frame_transfer as rft
import math

"Test 1: when rotations are applied, they yield the expected results"
r = [8000, 0, 0]
v = [0, 7.0587, 0]

pointing_vector_eci = [1, 0, 0]
# it is expected that this data, based on a circular orbit, yield a pointing vector in the RPY frame of [0, 0, -1],
# since the pointing vector in ECI is azimuthally pointing.
pointing_vector_rpy = rft.eci_to_rpy(pointing_vector_eci,r,v)
print(pointing_vector_rpy)

if all(pointing_vector_rpy == [0, 0, -1]) == 1:
    print("eci_to_rpy works correctly")
else:
    err1 = "eci_to_rpy does not work correctly"
    print("Error:", err1)

pointing_vector_rpy2 = [0.7071, 0.07071, 0]
# it is expected that using rpy_to_eci in this case yields the vector [0, 0.7071, -0.7071].
pointing_vector_eci2 = rft.rpy_to_eci(pointing_vector_rpy2, r, v)
print(pointing_vector_eci2)

if all(pointing_vector_eci2 - [0, 0.7071, -0.7071] < 0.001):
    print("eci_to_rpy works correctly")
else:
    err2 = "eci_to_rpy does not work correctly"
    print("Error:", err2)

pointing_vector_rpy3 = [0.57735, 0.57735, 0.57735]
euler_angles_in_rad = [math.pi/4, math.pi/4, math.pi/4]
# to check from external source that the result is correct
pointing_vector_body = rft.rpy_to_body(pointing_vector_rpy3, euler_angles_in_rad)
print(pointing_vector_body)

if all(pointing_vector_body - [0.1691019, 0.6969231, 0.6969231] < 0.001):
    print("rpy_to_body works correctly")
else:
    err3 = "rpy_to_body does not work correctly"
    print("Error:", err3)

pointing_vector_body2 = [0.57735, 0.57735, 0.57735]
euler_angles_in_rad2 = [math.pi/6, math.pi/6, math.pi/6]
# to check from external source the result
pointing_vector_rpy4 = rft.body_to_rpy(pointing_vector_body2, euler_angles_in_rad2)
print(pointing_vector_rpy4)

if all(pointing_vector_rpy4 - [0.66885631, 0.63018119, 0.39433738] < 0.001):
    print("rpy_to_body2 works correctly")
else:
    err4 = "rpy_to_body2 does not work correctly"
    print("Error:", err4)