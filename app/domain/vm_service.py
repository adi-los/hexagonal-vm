import subprocess
import os
from app.models.vm_request import VMCreateRequest

class VMService:
    def create_vm(self, vm_request: VMCreateRequest):
        vm_request_dict = vm_request.dict()

        # Use the relative path for the templates directory
        template_file = os.path.join("templates_vms", f"{vm_request.template_name}.cfg")

        if not os.path.exists(template_file):
            raise FileNotFoundError(f"Template {vm_request.template_name}.cfg does not exist.")

        with open(template_file, "r") as f:
            ks_template = f.read()

        # Replace variables in the template with provided values
        ks_config = ks_template.format(**vm_request.dict())

        # Write the modified content to ks.cfg
        ks_cfg_path = "templates_vms/ks.cfg"
        with open(ks_cfg_path, "w") as f:
            f.write(ks_config)

        # Construct the virt-install command
        command = [
            "virt-install",
            "--memory", str(vm_request.RAM),
            "--vcpus", str(vm_request.CPU),
            "--location", "/var/lib/libvirt/boot/Rocky-8.10-x86_64-minimal.iso",
            "--disk", f"path=/var/lib/libvirt/images/{vm_request.hostnamevm}.qcow2,size={str(vm_request.size)}",
            "--network", f"bridge={vm_request.tenant_name},virtualport_type=openvswitch",
            "--autostart",
            "--name", vm_request.hostnamevm,
            "--os-type", "linux",
            "--os-variant", "centos8",
            "--graphics=none",
            "--initrd-inject", ks_cfg_path,
            "--extra-args", "console=ttyS0 inst.text inst.ks=file:/ks.cfg",
            "--noautoconsole"
        ]

        # Print the command for debugging purposes
        print(f"Running command: {' '.join(command)}")

        try:
            subprocess.run(command, check=True)
            return {"message": f"Virtual machine {vm_request.hostnamevm} created successfully!"}
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Error creating virtual machine: {str(e)}")
