import serial
import serial.tools.list_ports
from tkinter import *
from tkinter import ttk
from functools import partial

# get all ports
ports = [x.device for x in serial.tools.list_ports.comports()]


def main():
    # set windows
    Window = Tk()
    Window.title('simulator')
    Window.geometry('768x512')
    Window.resizable(False, False)
    init(Window)
    Window.mainloop()


def init(Window):
    # select port text
    port_options_text = Label(
        Window, text='port', width=10)
    port_options_text.grid(row=0, column=0)
    # select port options
    port_options = ttk.Combobox(Window, width=10)
    port_options['value'] = ports
    port_options.current(0)
    port_options.grid(column=0)
    # set baud text
    port_baud_text = Label(
        Window, text='baud', width=10)
    port_baud_text.grid(column=0)
    # set baud input box
    port_baud = Entry(Window, width=14)
    port_baud.insert(0, 115200)
    port_baud.grid(column=0)
    # set timeout text
    port_time_out_text = Label(Window, text='time out(s)', width=10)
    port_time_out_text.grid(row=5, column=0)
    # set timeout options
    port_time_out = ttk.Combobox(Window, width=10)
    port_time_out['value'] = [x*5 for x in range(0, 25)]
    port_time_out.current(0)
    port_time_out.grid(column=0)
    # set xonxoff text
    port_xonxoff_text = Label(Window, text='xonxoff', width=10)
    port_xonxoff_text.grid(column=0)
    # set xonxoff options
    port_xonxoff = ttk.Combobox(Window, width=10)
    port_xonxoff['value'] = ['off', 'on']
    port_xonxoff.current(0)
    port_xonxoff.grid(column=0)
    # set rtscts text
    port_rtscts_text = Label(Window, text='rtscts', width=10)
    port_rtscts_text.grid(column=0)
    # set rtscts options
    port_rtscts = ttk.Combobox(Window, width=10)
    port_rtscts['value'] = ['off', 'on']
    port_rtscts.current(0)
    port_rtscts.grid(column=0)
    # set dsrdtr text
    port_dsrdtr_text = Label(Window, text='dsrdtr', width=10)
    port_dsrdtr_text.grid(column=0)
    # set dsrdtr options
    port_dsrdtr = ttk.Combobox(Window, width=10)
    port_dsrdtr['value'] = ['off', 'on']
    port_dsrdtr.current(0)
    port_dsrdtr.grid(column=0)
    # blank place holder to have one line empty
    blank = Label(Window, text='', width=10)
    blank.grid(column=0)
    # confirm button
    comfirm_button = Button(Window, text='comfirm', width=10, command=comfirm)
    comfirm_button.grid(column=0)
    # reset button
    reset_button = Button(Window, text='reset', width=10,
                          command=partial(reset, Window))
    reset_button.grid(column=0)
    # recv_test
    recv_text = Label(Window, text='recv', width=10)
    recv_text.grid(row=0, column=1, columnspan=20)
    # scrollable display
    port_recv_buffer = Text(Window, state='disabled')
    port_recv_buffer.grid(row=1, column=1, rowspan=20)
    for x in range(100):
        port_recv_buffer.configure(state='normal')
        port_recv_buffer.insert(END, str(x)+"\n")
        port_recv_buffer.configure(state='disabled')
    # send test
    send_text = Label(Window, text='send', width=10)
    send_text.grid(column=0, columnspan=2)
    # input box
    port_send_buffer = Text(Window, height=5)
    port_send_buffer.grid(column=0, columnspan=2)


def comfirm():
    print('comfirm')


def reset(Window):
    for widget in Window.winfo_children():
        widget.destroy()
    init(Window)


if __name__ == '__main__':
    main()
