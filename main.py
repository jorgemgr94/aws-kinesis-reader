from pynesis.streams import KinesisStream
import threading


def read_locations():
    # Get a reference to the stream we want to work with
    stream_locations = KinesisStream("Locations", region_name="us-east-1")

    # write on stream
    # stream.put("key", "my message".encode("utf-8"))

    # Read from streams
    for record in stream_locations.read():
        print(record)


def read_temperature():
    stream_temperature = KinesisStream("Temperature", region_name="us-east-1")
    for record in stream_temperature.read():
        print(record)


def main():
    t1 = threading.Thread(target=read_locations, args=[])
    t2 = threading.Thread(target=read_temperature, args=[])
    t1.start()
    t2.start()


if __name__ == "__main__":
    main()
