# Virtualization & Image Concepts

A practical guide to understanding ISO, QCOW2, QEMU, KVM, Docker, and related tools — especially in the context of building VM images with Packer.

---

## Table of Contents

1. [Big Picture: How Everything Fits Together](#big-picture)
2. [ISO — The OS Installer](#iso)
3. [QCOW2 — The Virtual Disk](#qcow2)
4. [QEMU — The VM Engine](#qemu)
5. [KVM — The Accelerator](#kvm)
6. [Docker — A Different Approach](#docker)
7. [Comparisons at a Glance](#comparisons)
8. [Packer Flow: Your Use Case](#packer-flow)
9. [Supporting Concepts](#supporting-concepts)

---

## Big Picture: How Everything Fits Together <a name="big-picture"></a>

When you run a virtual machine, several layers stack on top of each other:

```
┌──────────────────────────────────┐
│         Host Machine             │
│   (Your laptop or server OS)     │
└────────────────┬─────────────────┘
                 │
         ┌───────▼───────┐
         │      KVM      │  ← Hardware acceleration (Linux kernel feature)
         └───────┬───────┘
                 │
         ┌───────▼───────┐
         │     QEMU      │  ← Software that runs the virtual machine
         └───────┬───────┘
                 │
         ┌───────▼───────┐
         │  QCOW2 File   │  ← Virtual hard disk stored on host
         └───────┬───────┘
                 │
         ┌───────▼───────┐
         │  Ubuntu Guest │  ← The operating system running inside the VM
         └───────────────┘
```

**How they work together**

When you use Packer with the QEMU builder:

Packer tells QEMU to start a VM
QEMU may use KVM for acceleration
The VM installs/configures your OS
The resulting disk is saved as a QCOW2 image

👉 So the flow is:

Packer → QEMU (+KVM) → outputs QCOW2 image

---

## ISO — The OS Installer <a name="iso"></a>

An ISO is a disc image of an operating system installer. Think of it as the CD/DVD you'd use to install Ubuntu on a physical machine — just in file form.

**What it contains:**
- OS installation files
- A bootloader to start the install process
- The setup/configuration wizard

**Role in the flow:**

```
ISO → Boot VM → Install OS → QCOW2 disk image
```

> The ISO is consumed during installation and is not needed again once the QCOW2 image is built.

---

## QCOW2 — The Virtual Disk <a name="qcow2"></a>

A QCOW2 file is a virtual hard disk. It lives on your host machine as a single file but acts as a full storage drive inside the VM.

**What it contains after installation:**
- The installed operating system (e.g., Ubuntu)
- All files, applications, and configurations
- Any changes made by your provisioning scripts

**Key concept:** Ubuntu is installed *inside* the QCOW2 file. The QCOW2 is the disk; Ubuntu lives on it.

**Persistence behavior:**

| Scenario | Data Persists? |
|---|---|
| Same QCOW2 reused across boots | Yes |
| QCOW2 file deleted | No — all data lost |
| Fresh build from ISO | No — starts clean |

**QCOW2 vs other virtual disk formats:**

| Format | Used By |
|---|---|
| QCOW2 | QEMU / KVM |
| VMDK | VMware |
| VDI | VirtualBox |
| RAW | Generic (fast, but no compression) |

---

## QEMU — The VM Engine <a name="qemu"></a>

QEMU (Quick EMUlator) is the software that creates and runs virtual machines. It emulates the hardware that the guest OS sees.

**What QEMU does:**
- Emulates CPU, RAM, disk controllers, and network interfaces
- Boots a guest OS from an ISO or an existing QCOW2
- Manages VM lifecycle (start, pause, stop)

QEMU can run entirely in software (slow) or delegate CPU instructions to KVM (fast).

---

## KVM — The Accelerator <a name="kvm"></a>

KVM (Kernel-based Virtual Machine) is a feature built into the Linux kernel. It allows QEMU to pass CPU instructions directly to the physical hardware instead of emulating them in software.

| Setup | Speed |
|---|---|
| QEMU alone (no KVM) | Slow — every CPU instruction is emulated |
| QEMU + KVM | Fast — hardware handles most instructions directly |

**Requirements:** KVM only works on Linux hosts with a CPU that supports hardware virtualization (Intel VT-x or AMD-V). Most modern CPUs do.

---

## Docker — A Different Approach <a name="docker"></a>

Docker is often compared to VMs, but it solves a different problem. Docker is for **running applications**, not for running full operating systems.

**Docker flow:**

```
Docker Image → Container → Application runs
```

**Key differences from a VM:**
- No OS boot sequence — containers start in milliseconds
- Shares the host machine's Linux kernel instead of running its own
- Much smaller footprint (MBs vs GBs)
- Less isolation than a full VM

---

## Comparisons at a Glance <a name="comparisons"></a>

### ISO vs Docker Image

| Feature | ISO Image | Docker Image |
|---|---|---|
| Purpose | Install a full OS | Run an application |
| Requires OS boot | Yes | No |
| Contains full OS | Yes | No (only app + libraries) |
| Startup time | Slow (minutes) | Fast (seconds) |
| Primary use case | VM creation | Containerized apps |

### VM vs Container

| Feature | VM (QEMU + KVM) | Container (Docker) |
|---|---|---|
| OS | Full OS per VM | Shared host OS kernel |
| Isolation | Strong | Medium |
| Startup speed | Slower | Very fast |
| Disk size | Large (GBs) | Small (MBs) |
| Best for | Full system control | Running apps quickly |

### When to use which

| Goal | Best Choice |
|---|---|
| Build a VM image for Packer or cloud | ISO + QCOW2 + QEMU + KVM |
| Run a full OS with complete isolation | VM |
| Run an application quickly | Docker container |
| Lightweight, reproducible environments | Docker container |
| Full system control and customization | VM |

---

## Packer Flow: Your Use Case <a name="packer-flow"></a>

**Using QEMU/KVM builder (ISO-based):**

```
ISO
 └─ QEMU + KVM boot the ISO
     └─ Ubuntu installs onto QCOW2 virtual disk
         └─ Provisioning scripts (.sh) run inside the VM
             └─ Final QCOW2 image is saved as output
```

**Using Docker builder:**

```
Base Docker image
 └─ Container is created
     └─ Commands / scripts run inside the container
         └─ New Docker image is saved as output
```

---

## Supporting Concepts <a name="supporting-concepts"></a>

### Bootloader

A bootloader is a small program that runs immediately after the machine powers on. Its job is to bridge the gap between firmware (BIOS/UEFI) and the operating system.

**Sequence:**
1. Power on
2. BIOS/UEFI initializes hardware
3. Bootloader runs
4. Bootloader locates and loads the Linux kernel into RAM
5. OS starts

---

### GRUB

GRUB (GNU GRand Unified Bootloader) is the standard bootloader for most Linux systems.

**What GRUB does:**
1. BIOS/UEFI hands control to GRUB
2. GRUB displays a menu (if multiple OSes are installed)
3. GRUB loads the selected Linux kernel into memory
4. The OS takes over

---

### UFW (Uncomplicated Firewall)

UFW is a command-line tool for managing Linux firewall rules. It wraps the lower-level `iptables` system with a simpler interface.

**Why it matters:**
By default, a Linux server exposes all its ports to the network. Without a firewall, services like SSH or MySQL can be attacked by anyone who can reach the server.

**What UFW lets you do:**
- Allow only the traffic you need (e.g., SSH on port 22, HTTP on port 80)
- Block everything else by default
- Add rate limiting to slow down brute-force login attempts

**Simple mental model:** UFW is a security guard at the door — it only lets in traffic you've explicitly approved.

**When not to use UFW:**
- In advanced networking setups where `iptables` or `nftables` are managed directly
- When a cloud provider's security groups are already handling traffic rules

---

### cloud-init

cloud-init is a system service that runs automatically when a VM first boots in a cloud environment. It is not part of your project — it comes pre-installed in cloud OS images (like Ubuntu AMIs on AWS).

**What cloud-init does on first boot:**
- Configures networking
- Sets the hostname
- Creates user accounts
- Runs any user-data scripts you provided at launch

**Why this matters for Packer:** cloud-init runs during the early boot phase and takes a few seconds to complete. Packer's SSH communicator needs to wait for this to finish before it can connect and run provisioners. This is why Packer templates often include a boot wait time.

---

### Common APT Commands Explained

```bash
apt -qqy update
```
- `apt update` — refreshes the local package repository index (does not install anything)
- `-qq` — quiet mode; suppresses most output
- `-y` — automatically answers "yes" to any prompts

```bash
apt-get -qqy clean
```
- Removes cached package `.deb` files downloaded during previous installs
- Frees disk space in the VM image (important for keeping image sizes small)

-------------

## Trivy scan

from start to finish to scan the nanoclaw image:


### Step 1 — Verify Trivy is available

```bash
/c/tools/trivy/trivy.exe --version
```

### Step 2 — Confirm the built image exists in the build folder

```bash
ls -lh /c/POC/packer_templates_newfold/packer_templates/templates/build/
```

### Step 3 — Check the image format (confirms it is qcow2)

```bash
qemu-img info "C:/POC/packer_templates_newfold/packer_templates/templates/build/nanoclaw-ubuntu-24.04-amd64"
```

### Step 4 — Convert qcow2 → raw

Required because Trivy on Windows cannot parse qcow2 directly.
The virtual size is 20G so the raw file will be ~20G on disk.

```bash
qemu-img convert \
  -f qcow2 \
  -O raw \
  "C:/POC/packer_templates_newfold/packer_templates/templates/build/nanoclaw-ubuntu-24.04-amd64" \
  "C:/POC/packer_templates_newfold/packer_templates/templates/build/nanoclaw-ubuntu-24.04-amd64.raw"
  ```

### Step 5 — Run Trivy VM scan and save results

```bash
cd /c/POC/packer_templates_newfold/packer_templates/templates

/c/tools/trivy/trivy.exe vm \
  --scanners vuln \
  --timeout 60m \
  --output "nanoclaw-trivy-scan.txt" \
  "build/nanoclaw-ubuntu-24.04-amd64.raw" \
  2>&1 | tee -a "nanoclaw-trivy-scan.txt"
  ```

### Step 6 — View summary of findings by severity

```bash
grep "^Total:" nanoclaw-trivy-scan.txt
```

### Step 7 — View only CRITICAL and HIGH vulnerabilities

```bash
/c/tools/trivy/trivy.exe vm \
  --scanners vuln \
  --severity HIGH,CRITICAL \
  --timeout 60m \
  --output "nanoclaw-trivy-scan-critical-high.txt" \
  "build/nanoclaw-ubuntu-24.04-amd64.raw" \
  2>&1 | tee -a "nanoclaw-trivy-scan-critical-high.txt"
  ```

### Optional — Clean up the raw file after scanning (saves ~20G disk space)

```bash
rm "C:/POC/packer_templates_newfold/packer_templates/templates/build/nanoclaw-ubuntu-24.04-amd64.raw"
```
Why each step is needed:

|Step	| Reason |
|--------|--------|
|qemu-img info|	Confirm format before converting|
|qemu-img convert|	Trivy vm on Windows requires a raw disk image — it cannot open qcow2 directly (Invalid master boot record signature error)|
|--scanners vuln|	Scan for vulnerabilities only (skips secrets/misconfig for a faster run)|
--timeout 60m	The 20 GB raw image + Java DB download takes several minutes|
|--output + tee	|Saves results to file and also prints to terminal simultaneously|
|--severity HIGH,CRITICAL|	Optional filtered run to focus on the most important findings|

## Image Validate

Steps for local testing : 
 
Powershell -> wsl -d Ubuntu
 
### step 1 - Go to working directory
cd "/templates"
 
### step 2 - Build the image
packer build tool-dir/template.json
 
### step 3 - Create cloud-init seed ISO for local manual boot
cloud-localds seed.iso build-init/user-data build-init/meta-data
 
### step 4 - Boot the built image manually with QEMU
qemu-system-x86_64 \
  -cpu max \
  -m 4096 \
  -smp 2 \
  -drive file=build/image-name,if=virtio \
  -cdrom seed.iso \
  -nic user,hostfwd=tcp::2222-:22,hostfwd=tcp::8069-:8069,hostfwd=tcp::8080-:80,hostfwd=tcp::8443-:443 \
  -nographic
 
 
### step 5 - Open another WSL terminal and prepare SSH key:
cd "/templates"
 
mkdir -p ~/.ssh
cp build-init/id_ed25519 ~/.ssh/id_ed25519_packer
chmod 600 ~/.ssh/id_ed25519_packer
 
### step 6 - SSH into the running VM
ssh -o StrictHostKeyChecking=no -i ~/.ssh/id_ed25519_packer root@127.0.0.1 -p 2222

## tools

### Paperclip

### Nanoclaw
