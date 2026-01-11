def clear_frame(content_frame):
    # destory every children
    for widget in content_frame.winfo_children():
        widget.destroy()

def network_scan(content_frame, ttk):
    clear_frame(content_frame)
    ttk.Label(content_frame, text="network scan").grid(row=1, column=1, sticky='w')

def port_scan(content_frame, ttk):
    clear_frame(content_frame)
    ttk.Label(content_frame, text="port_scan").grid(row=1, column=1, sticky='w')

def arp_spoofing(content_frame, ttk):
    clear_frame(content_frame)
    ttk.Label(content_frame, text="arp spoofing").grid(row=1, column=1, sticky='w')

def dns_poison(content_frame, ttk):
    clear_frame(content_frame)
    ttk.Label(content_frame, text="dns poison").grid(row=1, column=1, sticky='w')