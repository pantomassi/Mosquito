from djitellopy import tello
import cv2
import time
import logging


# https://djitellopy.readthedocs.io/en/latest/tello/#djitellopy.tello.Tello


class Mosquito(tello.Tello):
    def __init__(self):
        self.drone = tello.Tello()
        self.drone.connect()
        self.drone.LOGGER.setLevel(logging.WARNING) # Original level INFO is good for debugging, but spams a lot
        self.drone.RESPONSE_TIMEOUT = 15
        self.drone.RETRY_COUNT = 5
        self.next_keep_alive_turn = "right"

    # Override due to continous error when exiting the app: __del__() calls end() that tries to reassign a non-existing attribute 'address' of Tello
    def __del__(self):
        return


    def check_temp_and_battery(self):
        """ The check is only informative and doesn't stop the app.
        """
        temperature = self.drone.get_temperature()
        battery = self.drone.get_battery()
        if temperature >= 85:
            print("[! ALERT !] The drone is overheating (+85 C).")
        if battery <= 20:
            print("[! ALERT !] The drone's battery is less than 20%. Consider landing.")


    def keep_alive_turn(self):
        """Keep the drone busy if no commands are passed to it to prevent auto-landing after 15s.
        """
        if self.next_keep_alive_turn == "right":
            self.drone.rotate_clockwise(1)
            self.next_keep_alive_turn = "left"
        else:
            self.drone.rotate_counter_clockwise(1)
            self.next_keep_alive_turn == "right"


    def screenshot(self):
        self.drone.streamon()
        screenshot_name = f"img_{time.strftime('%Y%m%d-%H%M%S')}"

        frame_read = self.drone.get_frame_read().frame
        cv2.imwrite(f"./screenshots/{screenshot_name}.png", frame_read)
        print(f" Screenshot {screenshot_name} taken.")
        self.drone.streamoff()


    # Press Q to end video stream.
    def start_video(self):
        self.drone.streamon()
        while True:
            screen = self.drone.get_frame_read().frame
            screen = cv2.resize(screen, (420, 300))
            cv2.putText(screen, f"Battery:{self.drone.get_battery()}", (10, 450), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255))
            cv2.imshow("Video_Stream (press Q to close)", screen)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print(" <Q> Exiting video stream.")
                break
        cv2.destroyAllWindows()
        self.drone.streamoff()


    def stop_video(self):
        pass


    def set_speed(self, speed):
        try:
            self.drone.set_speed(speed)
        except Exception as e:
            print(f"[SET_SPEED ERROR] Speed is allowed in the range <20-100>cm/s. Got: {speed}. Details: {e} / {e.__class__.__name__}")


    # Passing only the first letter of flip direction - see Djitellopy method
    def flip(self, direction):
        try:
            self.drone.flip(direction[0])
        except Exception as e:
            print(f"[FLIP ERROR] Details: {e} / {e.__class__.__name__}")


    # Djitellopy allows 20-500cm movement at once. Max 999cm per voice command
    def go(self, direction, distance):
        try:
            if distance != 0 and 20 <= distance <= 999:
                if distance > 500:
                    self.drone.move(direction, 480)    # 480 to not error out when distance is <500,520>
                    self.drone.move(direction, distance-480)
                else:
                    self.drone.move(direction, distance)
            else:
                print(f"Distance must be in range <20, 999>. Got: {distance}cm.")
        except Exception as e:
            print(f"[MOVE ERROR] Details: {e} / {e.__class__.__name__}")


    def turn(self, direction, degree): 
        try:
            if direction == "back":
                return self.drone.rotate_counter_clockwise(180)
            if 0 < degree <= 360:
                if direction == "right":
                    self.drone.rotate_clockwise(degree)
                elif direction == "left":
                    self.drone.rotate_counter_clockwise(degree)
            else:
                print(f"Turn degree must be a valid number from range <1, 360>. Got: {degree}.")
        except Exception as e:
            print(f"[TURN ERROR] Details: {e} / {e.__class__.__name__}")
