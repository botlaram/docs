# Packer




- [Packer](#packer)
  - [What is Packer?](#what-is-packer)
  - [Stages of Packer](#stages-of-packer)
  - [Usage of Packer](#usage-of-packer)
    - [Mutable and Immutable stage](#mutable-and-immutable-stage)
      - [Mutable](#mutable)
      - [Immutable](#immutable)


## What is Packer?

Packer is a tools which help to create customize Image from multiple platform from a single source configuration.

![PAcker](./png/packer.png)

## Stages of Packer

![PAcker](./png/stage-define.png)

## Usage of Packer

### Mutable and Immutable stage

WHY to use PACKER.????

- Well there are to stages of create Images > Mutable and Immutable

- Mutable means changing Continuosly.

- Immutable means needs to configure only one time.

- Mutable is old way to configure the Images.

- Where it needs to cofingure after deploying the application 

- If any case, we want to deploy to multiple server, configure multiplt server individually may create new bugs.

- Where as Packer use Immutable, which is configure deploy deplying to server.

- Using single configure Image we can spin up multiple server.

#### Mutable

**DEPLOY > SERVER > CONFIGURE**

![Mutable](./png/mutable1.png)

Configuring after spinning up server, If any case we need to install dependency into that server
we need to isntall it each individual server, which can lead to issues and Bugs.

![Mutable](./png/mutable2.png)

#### Immutable

**DEPLOY > CONFIGURE > SERVER**

![imMutable](./png/immutable1.png)

In Immutable Deploying and Configuration is done before hosting to server

![imMutable](./png/immutable2.png)

In Immutable using One Packer we can spin up multiple server

![imMutable](./png/immutable3.png)
