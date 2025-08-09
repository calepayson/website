---
title: Darwin Machines
slug: darwin_machines.md
description: Ramblings on William Calvin's theory of Darwin Machines.
date_created: 2024-07-16
date_modified: 2025-07-30
draft: false
---

# Darwin Machines

I'm writing this because I've been obsessed with the theory of a Darwin Machine
for nearly a year now and I haven't met anyone else who has heard of it.

This is my attempt to summarize and share the theory that William Calvin laid
out in "The Cerebral Code". If you haven't read it and are interested in how the
brain works, AI, or ML you should order a copy right now. I'm going to do the
book no justice but hopefully, if you haven't already ordered the book, the rest
of this post will convince you to read it.

If you, or anyone you know, is interested in these ideas or wants to build/is
building a Darwin Machine, please reach out. My email is calepayson(at)mac.com.

## Some Background

### On Evolution:

Near the end of his career Schrodinger wrote a book, "What is Life?", that
provides a great lens through which to view biology: Life is unnatural... If
you're a physicist.

One of the defining pillars of physics is the second law of thermodynamics.
Energy hates being concentrated. Yet here we are, squishy bags of water and
energy suspended a few feet above the ground. It's a bit weird.

Schrodinger decided the only way that life was possible was if it led to more
entropy throughout the system. Like a tornado, life is a pocket of order that
sows disorder. It lives so long as it pays the entropy tax.

To anthropomorphize a bit, The Universe is trying to maximize entropy but it has
a near infinite "problem space". One algorithm it has found to solve this
problem is evolution. To butcher a computer science phrase, I believe that
evolution is the "best case runtime" when trying to find increasingly valid
solutions to a near infinite problem space.

Essentially, biology uses evolution because it is the best way to solve the
problem of prediction (survival/reproduction) in a complex world.

### On Constraints

I love constraints in science because they can give us hope for a theory before
it has been worked out. For example, before we knew what genetic material, we
knew it had to fit in cells, be chemically stable, and had to be capable of
making high fidelity copies of itself. It took four years after Watson and
Crick discovered the double helix for us to prove it was genetic material but
we knew their discovery held promise because it fit within the constraints.

I see a few constraints governing how the brain works.

First, and most importantly, the brai is also faced with a near infinite problem
space. There are limitless behaviors, only some of which are "fit" for any
given scenario. Any theory of intelligence should explain how the brain solves
this in the most efficient manner possible.

The other constraints are based on a few studies and observations that seem
important.

Karl Lashley showed that memory is massively parallel and, contrary to the idea
of a "grandmother cell", is not stored in a single location.

David Eagleman showed that other function in the brain, like perception, are
also massively parallel.He dubbed this the "Mr. Potato Head" theory because no
matter where you "plug in" sensory input, your brain tends to figure out what
to do with it. Plug some eyes into the olfactory cortex and a nose in the visual
cortex and the brain will keep right on trucking.

Two additional things to add:

Brain patterns are spatio-temporal patterns. If I turn off cell firings, say
with anesthesia, you lose your train of thought.

But they store those patterns spatially. When you come out of anesthesia, you're
still you.

Think of it like RAM vs. Disk.

### On Brains

If you were to flatten out the neocortex of the brain - the new bit that we
think is important for intelligence - on a table you would notice two things.

First, if you look at a cross-section of the brain (eye-level with the table),
the brain is divided into ~6 layers. This layering forms the dominant narrative
of how intelligence may work and is the basis for deep neural nets. The idea is,
stimulus is piped into the "top" layer and filters down to the bottom layer,
with each layer picking up on more and more abstract concepts. Three Blue One
Brown does a good job of articulating this idea in a [video](https://youtu.be/aircAruvnKk?si=MMZ_O7NATm38f_DT&t=332).

Second, if you look down on the brain from above, it's divided into columns. The
smallest unit of these are minicolumns, bundles of 80-120 neurons that run
perpendicular to the layers of the brain, from the "top" to the "bottom" (or
vice versa, it doesn't matter). These minicolumns can then be grouped into
cortical columns, roughly hexagonal bundles of minicolumns, also running
perpendicular to the layers of the brain.

And that's about it. The brain is incredibly, wonderfully complex. The neocortex
is insanely complex too. And... it's also basically a crumpled up sheet with the
structure described above. At least that's the level of abstraction we're
working with.

From the perspective of a bystander, moderen machine learning seems to believe
that the recipe for more intelligence is adding more layers or depth. But based
on the homogeneity of the neocortex it seems that, at least in biology, the
recipe for more intelligence is adding more columns side by side. A rat has the
same number of layers as a chimp as a human, but the surface area of a rat's
neocortex, a proxy for the number of columns, is less than a chimp which is less
than a human.

To prevent confusion, I'm saying that adding more columns is the recipe for more
"animal intelligence". "Human intelligence" is different than animal
intelligence owing to our capacity for high fidelity imitation. I plan on
writing more on this in the future.

## On Darwin Machines

If modern ML explains intelligence with layers, the theory of a Darwin Machine
explains intelligence with columns.

As a reminder, a theory for intelligence should satisfy the following:

1. Implements an efficient algorithm to search a near infinite problem space.
2. Both memory and processing are massively parallel.
3. Computation uses spatio-temporal patterns.
4. But memory is spatial.

The theory of Darwin Machines developed by William Calvin proposes that the
brain, like life, implements evolution to search a near infinite problem space.

Calvin believes that minicolumns are the arena for this evolution. Sensory
inputs hit the brain, visual input in one area, olfactory in another, etc. and
trigger specific firing patterns in the minicolumns. Imagining the surface of
brain laid flat on a table, we can look down on it and see these columns
lighting up, as if with Morse Code messages. These messages then propagate
across the surface area of the brain, competing with conflicting messages to
take over the greatest surface area.

After some period of time a winner is chosen, let's say the message that
controls the greatest surface area, the greatest number of minicolumns. When
this happends, the winning minicolumns are rewarded, likely prompting them to
encode a tendency for that firing pattern into their structure.
