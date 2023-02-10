# Server Documentation

## Server Class Diagram

![server_class_diagram](./Server%20Class%20Diagram.jpg)

### DjangoConnection

DjangoConnection 클래스는 Django 서버와 소켓을 통한 통신을 담당한다.
채널생성, 채널참여 데이터를 요청받으면, RoomManager 클래스의 메서드를 호출한다.

#### fields



#### methods


### RoomManager

채널 생성, 채널 참여, 채널 삭제 등 채널을 관리하는 클래스이다.


#### fields

    - gameList: List[GameManager]
        생성된 채널들을 담고 있다.

#### methods

    - create_room(HostPlayer): Room
        호스트플레이어를 방장으로 하는 채널을 하나 생성한다.
        생성한 채널은 GameManager로 래핑하여 gameList에 추가한다.

    - addPlayer(Room, Player)
        해당 방에 플레이어를 추가한다.

### GameManager

각 채널마다의 플레이 순서, 현재 상황(어떤 플레이어가 어떤 콜을 했고, 누구의 차례인지) 등을 담고 있다.

#### fields

    - room: Room
        해당 채널의 room 객체를 담는다.

#### methods

    - addPlayer(Player)
        현재 방에 플레이어를 추가한다.
    
    - delPlayer(Player)
        현재 방에 플레이어를 추방한다.

    - bet(Player, BetCall): Player
        해당 플레이어가 해당 콜을 했음을 처리한다.
        다음 배팅을 해야 할 플레이어를 반환한다.

### ClientConnection

소속된 GameManager 클래스에 해당하는 방의 각 플레이어와 Websocket 통신을 담당한다.

#### fields

    - player: Player
        연결된 플레이어의 객체

#### methods

    - bet_request()
        현재 배팅 순서임을 전송한다.

    - send_bet_data()
        다른 플레이어가 어떤 배팅을 했는지 전송한다.

    - send_room_data()
        방 상세설정(순서, 배팅방식 등)이 바뀌었을 경우, 이를 전송한다.
