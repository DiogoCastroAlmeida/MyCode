import argparse
import backend
import sys


class ArgumentsParser():
    def __init__(self, args): #the args paramater must be a list
        DESCRIPTION = """\
Internet Tools to get information about ip addrs, hostnames, ports and services"""
        self.parser = argparse.ArgumentParser(description=DESCRIPTION)
        self.args=args


    def define_arguments(self):
        self.parser.add_argument("-hn", "--hostname", action="store_true",
                                help="Gets this machine's hostname.")
        self.parser.add_argument("-sp", "--service-port", action="store",
                                help="Gets the name of a service based on it's port number.")
        self.parser.add_argument("-ps", "--port-service", action="store",
                                help="Gets the port of a service based on it's name number")
        self.parser.add_argument("-e", "--extended", action="store_true",
                                help="Print extended information. Will be ignored with '-sp', '-ps' and '-o'.")
        self.parser.add_argument("-ghn", "--get-hostname", action="store",
                                help="Gets the hostname of an IP Addr. With the '-e', prints alternativess alias for the hostname and alternative IP Addrs for the specified IP Addr.")
        self.parser.add_argument("-gip", "--get-ip", action="store",
                                help="Gets the IP Addr of an hostname. With the '-e', prints alternativess alias for the hostname and all IP Addrs for the specified hostname.")
        self.options = self.parser.parse_args(self.args)


    def exec_o(self):
        if self.options.hostname:
            backend.get_my_hostname()


    def exec_sp_ps(self):
        #as the parses for both this arguments are similar, this function will hanndle both
        def do_parse(options_var, backend_func):
            if options_var != None:
                backend_func(options_var)

        do_parse(self.options.service_port, backend.get_service_by_port)
        do_parse(self.options.port_service, backend.get_port_by_service)


    def exec_gi_gd(self): #for the get_ipaddr() and get_dn() functions in the backend package
        def do_parse(options_var, bool_var, backend_func):
            if options_var != None:
                backend_func(options_var, bool_var)

        do_parse(self.options.get_hostname, self.options.extended, backend.get_hostname)
        do_parse(self.options.get_ip, self.options.extended, backend.get_ipaddr)


    def make_output(self):
        self.exec_o()
        self.exec_sp_ps()
        self.exec_gi_gd()


a = ArgumentsParser(sys.argv[1::])
a.define_arguments()
a.make_output()
