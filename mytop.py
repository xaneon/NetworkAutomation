from mininet.topo import Topo


class Kap5_SDN_mytop(Topo):
    def __init__(self):

        Topo.__init__(self)

        # Add switches
        switchN = self.addSwitch('sN', dpid='1')
        switchNW = self.addSwitch('sNW', dpid='2')
        switchNE = self.addSwitch('sNE', dpid='3')
        switchSW = self.addSwitch('sSW', dpid='4')
        switchSE = self.addSwitch('sSE', dpid='5')

        # Add hosts
        hostN1 = self.addHost('hN1')
        hostNW1 = self.addHost('hNW1')
        hostNE1 = self.addHost('hNE1')
        hostSW1 = self.addHost('hSW1')
        hostSE1 = self.addHost('hSE1')

        # Connect Switches
        self.addLink(switchN, switchNW)
        self.addLink(switchN, switchNE)
        self.addLink(switchNW, switchNE)
        self.addLink(switchNW, switchSW)
        self.addLink(switchNW, switchSE)
        self.addLink(switchNE, switchSW)
        self.addLink(switchNE, switchSE)
        self.addLink(switchSW, switchSE)

        # Connect Hosts
        self.addLink(hostN1, switchN)
        self.addLink(hostNW1, switchNW)
        self.addLink(hostNE1, switchNE)
        self.addLink(hostSW1, switchSW)
        self.addLink(hostSE1, switchSE)


topos = {'mytopo': (lambda: Kap5_SDN_mytop())}
